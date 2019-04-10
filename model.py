import os

import pandas as pd
import tensorflow as tf
from tensorflow import keras

from utils import save_embeddings

from keras.preprocessing.text import Tokenizer

current_directory = os.getcwd()
train_data = pd.read_csv(current_directory + "/data/DataTurks/dump.csv")


if __name__ == '__main__':

    save_word_embeddings = True
    train_data = train_data.sample(frac=1).reset_index(drop=True)

    X_train = train_data['content'][:18000]
    X_test = train_data['content'][18000:]

    y_train = train_data['label'][:18000]
    y_test =  train_data['label'][18000:]


    tokenizer = Tokenizer(num_words=10000)
    tokenizer.fit_on_texts(train_data['content'])

    train_sequences = tokenizer.texts_to_sequences(X_train.values)
    test_sequences = tokenizer.texts_to_sequences(X_test.values)

    vocab_size = 10000

    padded_train = keras.preprocessing.sequence.pad_sequences(train_sequences, padding='post',
                                                              maxlen=140)
    padded_test = keras.preprocessing.sequence.pad_sequences(test_sequences, padding='post',
                                                              maxlen=140)

    model = keras.Sequential()
    model.add(keras.layers.Embedding(vocab_size, 40))
    model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense(4, activation=tf.nn.relu))
    model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

    model.summary()

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

    split = int(len(X_train) / 4 )  # number of comments halved

    x_val = padded_train[:split]
    partial_x_train = padded_train[split:]

    y_val = y_train[:split]
    partial_y_train = y_train[split:]

    history = model.fit(partial_x_train, partial_y_train, epochs=120, batch_size=512, validation_data=(x_val, y_val),
                        verbose=1)


    if save_word_embeddings == True:
        word_index = tokenizer.word_index
        save_embeddings(model, word_index)


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



