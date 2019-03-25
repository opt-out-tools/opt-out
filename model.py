import pandas as pd
import numpy as np
# TODO needs improving
from normalize import normalize
from tensorflow import keras


def enumerate_corpus(corpus):
    """ Used to create a look up table for the vocabulary for later conversion back to the original sentence
    """
    return {k: v for k, v in enumerate(corpus)}


def test_enumerate_corpus():
    assert enumerate_corpus(["figured", "apple"]) == {0: "figured", 1: "apple"}


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

    vocab_size = len(corpus)
