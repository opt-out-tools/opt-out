import os

import pandas as pd
import tensorflow as tf
from tensorflow import keras

from dictionary import *
from normalize import normalize

current_directory = os.getcwd()
train_data = pd.read_csv(current_directory + "/data/train.csv")
test_data = pd.read_csv(current_directory + "/data/test_with_solutions.csv")


def prepare_data(df):
    """Returns a data frame prepared for word padding.

    This is achieved by normalizing the comments and enumerating the remaining words

    Args:
        df: The data frame

    Returns:
        df (dataframe): A prepared data frame
        dictionary (dict): A dictionary of the corpus vocabulary enumerated

    """

    df["Normalized"] = df["Comment"].apply(normalize)

    corpus = [sentence for comment in df["Normalized"].tolist() for sentence in comment]
    dictionary = rank_corpus(corpus)

    df["Enumerated"] = df["Normalized"].apply((lambda comment: enumerate_comment(comment, dictionary)))

    return df, dictionary


def test_prepare_data_creates_necessary_columns():
    df = train_data

    assert prepare_data(df)['Normalized'].all() == df['Normalized'].all()
    assert prepare_data(df)['Enumerated'].all() == df['Enumerated'].all()


if __name__ == '__main__':
    train, train_dict = prepare_data(train_data)
    test, test_dict = prepare_data(test_data)

    vocab_size = len(train_dict)

    padded_train = keras.preprocessing.sequence.pad_sequences(train["Enumerated"].values, padding='post',
                                                              maxlen=140)
    padded_test = keras.preprocessing.sequence.pad_sequences(test["Enumerated"].values, padding='post',
                                                              maxlen=140)

    model = keras.Sequential()
    model.add(keras.layers.Embedding(vocab_size, 4))
    model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense(4, activation=tf.nn.relu))
    model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

    model.summary()

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

    mid = int(3947 / 2)  # number of comments halved

    x_val = padded_train[:mid]
    partial_x_train = padded_train[mid:]

    y_val = train['Insult'][:mid]
    partial_y_train = train['Insult'][mid:]

    history = model.fit(partial_x_train, partial_y_train, epochs=40, batch_size=512, validation_data=(x_val, y_val),
                        verbose=1)

    predicted_sentiment_score = model.predict(padded_test)

    history_dict = history.history
    history_dict.keys()

    import matplotlib.pyplot as plt

    acc = history_dict['acc']
    val_acc = history_dict['val_acc']
    loss = history_dict['loss']
    val_loss = history_dict['val_loss']

    epochs = range(1, len(acc) + 1)

    # "bo" is for "blue dot"
    plt.plot(epochs, loss, 'bo', label='Training loss')
    # b is for "solid blue line"
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()

    plt.clf()  # clear figure

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.show()
