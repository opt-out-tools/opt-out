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

    vocab_size = len(corpus)

    train_data = keras.preprocessing.sequence.pad_sequences(train["Enumerated"].values, padding='post')
