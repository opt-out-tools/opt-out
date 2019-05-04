import os

import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from tensorflow import keras

from parseargs import ParseArgs
from utils import save_embeddings
from visualization import plot_loss, plot_accuracy


class Model:

    def __init__(self):
        pass

    def create_dictionary(self, data, n_words):
        """Prepares the corpus for the model and returns the Tokenizer object.
        Args:
            data (pandas series) : The column of text to be classified.
            n_words (int) : This argument will keep the most frequent n_words in the training data.

        Returns:
            tokenizer (Tokenizer) :
        """
        tokenizer = Tokenizer(num_words=n_words)
        tokenizer.fit_on_texts(data)
        return tokenizer

    def split(self, data):
        """Randomly shuffles the data and splits it into train and test.
        Args:
            data (df) : The entire dataset.

        Returns:
            train (df) : The training data.
            test (df)  : The test data.
        """
        where_to_split = int(len(data) * 0.8)
        shuffled_data = data.sample(frac=1).reset_index(drop=True)
        train = shuffled_data[:where_to_split]
        test = shuffled_data[where_to_split:]
        return train, test

    def build(self, path_to_data, text_column_name, label_column_name, hyperparameters, save_word_embeddings,
              save_model):
        """Returns the built model. This function prepares the text, turns them into tensors, creates a word embedding
        and trains the neural net and build the final model. There are two flags that allow the embeddings and the
        model to be saved.

        Args:
            path_to_data (str) : The path to the dataset from the current directory.
            text_column_name (str) : The name of the column of the dataset with the text to be classified
            label_column_name (str) : The name of the column of labels.
            args
            save_word_embeddings (bool) : If true, will save the embedding data.
            save_model (bool) : If true, will save the model with a system timestamp in the name..

        Returns
            model : The sentiment analyser model, fit to the training data.
        """
        data = pd.read_csv(os.getcwd() + path_to_data)

        corpus_vocabulary = self.create_dictionary(data[text_column_name], hyperparameters['vocab_size'])

        train, test = self.split(data)

        X_train = train[text_column_name]
        y_train = train[label_column_name]

        train_sequences = corpus_vocabulary.texts_to_sequences(X_train.values)
        padded_train = keras.preprocessing.sequence.pad_sequences(train_sequences, padding='post',
                                                                  maxlen=140)
        model = keras.Sequential()
        model.add(keras.layers.Embedding(hyperparameters['vocab_size'], 40))
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

        model.fit(partial_x_train, partial_y_train, epochs=hyperparameters['epoch'],
                  batch_size=hyperparameters['batch_size'], validation_data=(x_val, y_val),
                  verbose=hyperparameters['verbose'])

        if save_word_embeddings is True:
            word_index = corpus_vocabulary.word_index
            save_embeddings(model, word_index)
            print('Word embeddings saved.')

        if save_model is True:
            import datetime as dt
            now = dt.datetime.now().__str__()
            model.save(os.getcwd() + '/saved_model_data/models/model_' + now + '.h5')
            print("Model saved.")

        return model

    def predict(self, test_sentence, model, corpus_vocabulary):
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

    def plot(self, model):
        """Plots the accuracy and loss of the validation and training."""
        history_dict = model.history.history
        history_dict.keys()

        epochs = range(1, len(history_dict['acc']) + 1)

        plot_accuracy(epochs, history_dict['acc'], history_dict['val_acc'])
        plt.clf()
        plot_loss(epochs, history_dict['loss'], history_dict['val_loss'])

    def evaluate(self, scores, targets):
        """Prints the f1-score and the confusion matrix for the model."""

        from sklearn.metrics import f1_score, confusion_matrix

        df = pd.DataFrame({"score": pd.Series(scores)})
        df.loc[df['score'] >= 0.5, 'label'] = 1
        df.loc[df['score'] < 0.5, 'label'] = 0

        print(f1_score(targets, df['label'].values))
        print(confusion_matrix(targets, df['label'].values))


if __name__ == '__main__':
    ParseArgs(Model())
