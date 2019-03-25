import pandas as pd
import numpy as np
from clean import escape_unicode


def normalize(comment):
    """
       # lowercase, tokenize, remove punctuation

    """
    tokenized_comment = list(map(lambda word: word.lower(), comment.split(' '))) # splits comment into words and makes each word lowercase

    PUNCTUATION = r"""[!"#$%&()*+,-./:;<=>?@[]^_`{|}~']"""

    return list(map(lambda word: word.translate(str.maketrans('', '', PUNCTUATION)), tokenized_comment)) # strips punctuation


def test_prep_comment():
    assert normalize("HELLO YOU! \\n") == ["hello", "you", "\\n"]


def test_prep_comment2():
    assert normalize("HELLO YOU! &") == ["hello", "you", ""]


def test_prep_comment3():
    assert normalize("\\xa0") == ["hello", "you", ""]


if __name__ == '__main__':
    import os

    current_directory = os.getcwd()
    test = pd.read_csv(current_directory + "/data/test_with_solutions.csv") # read in test data
    train = pd.read_csv(current_directory  + "/data/train.csv") # read in train data

    train['Tokenized'] = train['Comment'].apply(escape_unicode)
    train['Tokenized'] = train['Tokenized'].apply(normalize)

    stopwords = np.loadtxt(current_directory + "/data/stopwords.txt", dtype=np.str) # read in stopwords
    train['Tokenized'] = train['Tokenized'].apply(lambda comment: [word for word in comment if word not in stopwords])
    #

