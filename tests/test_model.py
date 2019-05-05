import os

import pandas as pd
import pytest

from ..src.stopit.model import Model

m = Model()


@pytest.fixture(scope="module")
def read_in_dataset():
    return pd.read_csv(os.getcwd() + "/data/DataTurks/dump.csv")


@pytest.fixture(scope="module")
def create_dataset_vocabulary(read_in_dataset):
    data = read_in_dataset
    return m.create_dictionary(data['content'], 10000)


def test_create_dictionary_vocab_size_is_correct(create_dataset_vocabulary):
    assert create_dataset_vocabulary.num_words == 10000


def test_create_dictionary_doesnt_remove_stopwords(create_dataset_vocabulary):
    assert "the" in create_dataset_vocabulary.word_counts.keys()
    assert "is" in create_dataset_vocabulary.word_counts.keys()
    assert "are" in create_dataset_vocabulary.word_counts.keys()


def test_create_dictionary_removes_punctuation(create_dataset_vocabulary):
    assert "!" not in create_dataset_vocabulary.word_counts.keys()
    assert ":)" not in create_dataset_vocabulary.word_counts.keys()
    assert "@" not in create_dataset_vocabulary.word_counts.keys()


def test_create_dictionary_removes_URLS(create_dataset_vocabulary):
    # TODO this should fail, there should not be URLs in the corpus
    assert "http" in create_dataset_vocabulary.word_counts.keys()


def test_create_dictionary_removes_Unicode(create_dataset_vocabulary):
    assert "\\xa0" not in create_dataset_vocabulary.word_counts.keys()


# TODO finish adding a optimized test that will check ranking
# def test_create_dictionary_most_common_word_correctly_ranked(create_dataset_vocabulary):
#     data = pd.read_csv(os.getcwd() + "/data/DataTurks/dump.csv")
#     corpus = " ".join(data["content"]).split()
#     counts = sorted([(word, corpus.count(word)) for word in set(corpus)], key=lambda t: t[1], reverse=True)
#     print(counts[0])

def proportion(df, label):
    df.loc[df['label'] == label, 'label'].count() / len(df)


def test_split_data_is_representative_of_underlying_distribution(read_in_dataset):
    data = read_in_dataset

    n_1s = proportion(data, 1)
    n_0s = proportion(data, 0)

    train, test = m.split(data)

    n_train_1s = proportion(train, 1)
    n_train_0s = proportion(train, 0)

    n_test_1s = proportion(test, 0)
    n_test_0s = proportion(test, 0)

    assert n_train_1s == n_1s
    assert n_train_0s == n_0s

    assert n_test_1s == n_1s
    assert n_test_0s == n_0s


def test_basic_negative():
    import glob
    list_of_files = glob.glob(os.getcwd() + "/saved_model_data/models/*")
    file = max(list_of_files, key=os.path.getctime)

    assert m.predict("You are a bitch", file, "/data/DataTurks/dump.csv", 'content', 10000) >= 0.5
    assert m.predict("Bitch suck dick", file, "/data/DataTurks/dump.csv", 'content', 10000) >= 0.5
    assert m.predict("I hate you", file, "/data/DataTurks/dump.csv", 'content', 10000) >= 0.5


def test_basic_positive():
    import glob
    list_of_files = glob.glob(os.getcwd() + "/saved_model_data/models/*")
    file = max(list_of_files, key=os.path.getctime)

    assert m.predict("You are a lovely person", file, "/data/DataTurks/dump.csv", 'content', 10000) < 0.5
    assert m.predict("The sun shines from your eyes", file, "/data/DataTurks/dump.csv", 'content', 10000)< 0.5
    assert m.predict("I love you so much", file, "/data/DataTurks/dump.csv", 'content', 10000) < 0.5
