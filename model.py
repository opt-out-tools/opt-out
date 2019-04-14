import os

import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from tensorflow import keras

from utils import save_embeddings
from visualization import plot_loss, plot_accuracy


def create_dictionary(data, n_words=10000):
    """Creates the internal vocabulary for the model and returns the Tokenizer object."""
    tokenizer = Tokenizer(num_words=n_words)
    tokenizer.fit_on_texts(data)
    return tokenizer


def test_tokenizer_size():
    tokenizer = create_dictionary(train_data['content'])
    assert tokenizer.num_words == 10000


def train(save_word_embeddings=False, plot_loss_acc=False):
    """Returns the sentiment of the parsed sentence.

    Args:
        save_word_embeddings (bool) : If true, will save the embedding data.
        plot_loss_acc (bool) : If true, will plot the loss and accuracy during the training of the data.

    Returns
        model : The sentiment analyser model, fit to the training data.
    """

    global train_data
    global corpus_vocabulary

    train_data = train_data.sample(frac=1).reset_index(drop=True)
    X_train = train_data['content'][:18000]
    y_train = train_data['label'][:18000]

    vocab_size = 10000

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

    history = model.fit(partial_x_train, partial_y_train, epochs=120, batch_size=512, validation_data=(x_val, y_val),
                        verbose=1)

    if save_word_embeddings == True:
        word_index = corpus_vocabulary.word_index
        save_embeddings(model, word_index)

    if plot_loss_acc == True:
        history_dict = history.history
        history_dict.keys()

        epochs = range(1, len(history_dict['acc']) + 1)

        plot_accuracy(epochs, history_dict['acc'], history_dict['val_acc'])
        plt.clf()
        plot_loss(epochs, history_dict['loss'], history_dict['val_loss'])

    return model


def test(test_sentence, model, corpus_vocabulary):
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

    return sentiment_score[0][0]


def test_basic_negative():
    from keras.models import load_model
    model = load_model("/saved_model_data/models/model_120.h5")

    global train_data

    tokenizer = create_dictionary(train_data['content'], 10000)
    assert test("You are a bitch", model, tokenizer) >= 0.5
    assert test("I hate you", model, tokenizer) >= 0.5


#  assert test("You are a cunt", model, tokenizer) >= 0.5


def test_basic_positive():
    from keras.models import load_model
    model = load_model("/saved_model_data/models/model_120.h5")

    global train_data

    tokenizer = create_dictionary(train_data['content'], 10000)
    assert test("You are a lovely person", model, tokenizer) < 0.5
    assert test("The sun shines from your eyes", model, tokenizer) < 0.5
    assert test("I love you so much", model, tokenizer) < 0.5


if __name__ == '__main__':
    train_data = pd.read_csv(os.getcwd() + "/data/DataTurks/dump.csv")
    corpus_vocabulary = create_dictionary(train_data['content'])

    model = train()
    print(test("You are a bitch", model, corpus_vocabulary))
