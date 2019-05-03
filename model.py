import os

import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from tensorflow import keras

from utils import save_embeddings, parse_args, Parse
from visualization import plot_loss, plot_accuracy

vocab_size = 10000


def create_dictionary(data, n_words):
    """Creates the internal vocabulary for the model and returns the Tokenizer object."""
    tokenizer = Tokenizer(num_words=n_words)
    tokenizer.fit_on_texts(data)
    return tokenizer


def split(dataframe, where_to_split):
    """Randomly shuffles the data and splits the data into train and test.
    Args:
        dataframe (df) : The data.
        where_to_split (int) : The size of the train data.

    Returns:
        train (df) : The training data.
        test (df)  : The test data.
    """
    shuffled_data = dataframe.sample(frac=1).reset_index(drop=True)
    train = shuffled_data[:where_to_split]
    test = shuffled_data[where_to_split:]
    return train, test


def build(train_data, save_word_embeddings=False, save_model=False):
    """Returns the sentiment of the parsed sentence.

    Args:
        train_data (df) : The data the model is to be built from.
        save_word_embeddings (bool) : If true, will save the embedding data.
        save_model (bool) : If true, will save the model.

    Returns
        model : The sentiment analyser model, fit to the training data.
    """
    global corpus_vocabulary

    X_train = train_data['content']
    y_train = train_data['label']

    vocab_size = 10000  # TODO automatic

    train_sequences = corpus_vocabulary.texts_to_sequences(X_train.values)
    padded_train = keras.preprocessing.sequence.pad_sequences(train_sequences, padding='post',
                                                              maxlen=140)
    model = keras.Sequential()
    model.add(keras.layers.Embedding(vocab_size, 40))
    model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense(4, activation=tf.nn.relu))
    model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

    model.summary()

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

    split = int(len(X_train) / 4)  # number of comments halved

    x_val = padded_train[:split]
    partial_x_train = padded_train[split:]

    y_val = y_train[:split]
    partial_y_train = y_train[split:]

    model.fit(partial_x_train, partial_y_train, epochs=1, batch_size=512, validation_data=(x_val, y_val),
              verbose=1)

    if save_word_embeddings == True:
        word_index = corpus_vocabulary.word_index
        save_embeddings(model, word_index)

    if save_model == True:
        import datetime as dt
        now = dt.datetime.now().__str__()
        model.save(os.getcwd() + '/saved_model_data/models/model_' + now + '.h5')
        print("Model saved.")

    return model


def predict(test_sentence, model, corpus_vocabulary):
    """Returns a sentiment score.

    Args:
        sentence (str) : The sentence to be analised.

    Returns:
        score (float) : The sentiment score of the sentence. 1 - cyber abusive, 0 - not cyber abusive.
    """
    parsed_test = pd.DataFrame({"content": pd.Series(test_sentence)})
    X_test = parsed_test['content']

    test_sequences = corpus_vocabulary.texts_to_sequences(X_test.values)

    padded_test = keras.preprocessing.sequence.pad_sequences(test_sequences, padding='post', maxlen=140)

    sentiment_score = model.predict(padded_test)

    return sentiment_score[:, 0]

def plot(model):
    """Plots the accuracy and loss of the validation and training."""
    history_dict = model.history.history
    history_dict.keys()

    epochs = range(1, len(history_dict['acc']) + 1)

    plot_accuracy(epochs, history_dict['acc'], history_dict['val_acc'])
    plt.clf()
    plot_loss(epochs, history_dict['loss'], history_dict['val_loss'])


def evaluate(scores, targets):
    """Prints the f1-score and the confusion matrix for the model."""

    global model
    global corpus_vocabulary

    from sklearn.metrics import f1_score, confusion_matrix

    df = pd.DataFrame({"score": pd.Series(scores)})
    df.loc[df['score'] >= 0.5, 'label'] = 1
    df.loc[df['score'] < 0.5, 'label'] = 0

    print(f1_score(targets, df['label'].values))
    print(confusion_matrix(targets, df['label'].values))


if __name__ == '__main__':
    data = pd.read_csv(os.getcwd() + "/data/DataTurks/dump.csv")
    corpus_vocabulary = create_dictionary(data['content'], vocab_size)

    train, test = split(data, 18000)

    model = build(train)
    plot(model)

    sentiment_scores = predict(test['content'], model, corpus_vocabulary)

    evaluate(sentiment_scores, test['label'])
