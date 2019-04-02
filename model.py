import pandas as pd
import numpy as np
# TODO needs improving
from normalize import normalize
from dictionary import *
from tensorflow import keras
import tensorflow as tf






if __name__ == '__main__':
    import os

    current_directory = os.getcwd()
    train = pd.read_csv(current_directory + "/data/train.csv")
    test = pd.read_csv(current_directory + "/data/test_with_solutions.csv")

    train["Tokenized"] = train["Comment"].apply(normalize)


    stopwords = np.loadtxt(current_directory + "/data/stopwords.txt", dtype=np.str)
    train["Tokenized"] = train["Tokenized"].apply(lambda comment: [word for word in comment if word not in stopwords])

    corpus = set([sentence for comment in train["Tokenized"].tolist() for sentence in comment])
    dictionary = enumerate_corpus(corpus)
    train["Enumerated"] = train["Tokenized"].apply((lambda comment: enumerate_comment(comment,dictionary)))
    train.to_csv(current_directory + "cleaned.csv")
    vocab_size = len(corpus)

    train_data = keras.preprocessing.sequence.pad_sequences(train["Enumerated"].values, padding='post')

    model = keras.Sequential()
    model.add(keras.layers.Embedding(vocab_size, 16))
    model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense(16, activation=tf.nn.relu))
    model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))

    model.summary()

    model.compile(optimizer='adam', loss='binary_crossentropy',  metrics=['acc'])

    mid = int(3947/2)
    x_val = train_data[:mid]
    partial_x_train = train_data[mid:]


    y_val = train['Insult'][:mid]
    partial_y_train = train['Insult'][mid:]

    history = model.fit(partial_x_train, partial_y_train, epochs=40, batch_size=512, validation_data=(x_val, y_val), verbose=1)

   # Evaluate

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
