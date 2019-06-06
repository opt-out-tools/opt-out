import os

import pandas as pd
import pytest

from models.neural_net.simple_dataturks import Model

m = Model()
path_to_data = "/models/neural_net/simple_dataturks_dict.csv"

@pytest.fixture(scope="module")
def read_in_dataset():
    return pd.read_csv(os.getcwd() + path_to_data)


@pytest.fixture(scope="module")
def create_dataset_vocabulary(read_in_dataset):
    data = read_in_dataset
    return m.create_dictionary(data['content'], 10000)

def test_basic_negative():
    path_to_model = os.getcwd() + "/models/neural_net/simple_dataturks.h5"

    assert m.predict("You are a bitch", path_to_model, path_to_data, 'content', 10000) >= 0.5
    assert m.predict("Bitch suck dick", path_to_model, path_to_data, 'content', 10000) >= 0.5
    assert m.predict("I hate you", path_to_model, path_to_data, 'content', 10000) >= 0.5


def test_basic_positive():
    path_to_model = os.getcwd() + "/models/neural_net/simple_dataturks.h5"

    assert m.predict("You are a lovely person", path_to_model, path_to_data, 'content', 10000) < 0.5
    assert m.predict("The sun shines from your eyes", path_to_model, path_to_data, 'content', 10000) < 0.5
    assert m.predict("I love you so much", path_to_model, path_to_data, 'content', 10000) < 0.5

