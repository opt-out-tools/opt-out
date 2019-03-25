import pandas as pd
import numpy as np
from clean import escape_unicode


def normalize(comment):
    """

    """
    # splits comment into words and makes each word lowercase
    tokenized_comment = list(map(lambda word: word.lower(), comment.split(" ")))

    cleaned_comment = escape_unicode(tokenized_comment)

    # strips punctuation & returns normalized comment
    return list(map(lambda word: word.translate(str.maketrans("", "", r"""[!"#$%&()*+,-./:;<=>?@[]^_`{|}~']""")), cleaned_comment))


def test_normalize_tokenize():
    assert normalize("HELLO YOU") == ["hello", "you"]


def test_normalize_unicode():
    assert normalize("HELLO YOU! \\n") == ["hello", "you", "\n"]


def test_normalize_punctuation():
    assert normalize("HELLO YOU! &") == ["hello", "you", ""]


if __name__ == '__main__':
    import os

    current_directory = os.getcwd()
    train = pd.read_csv(current_directory  + "/data/train.csv") # read in train data
    test = pd.read_csv(current_directory + "/data/test_with_solutions.csv") # read in test data

    train['Tokenized'] = train['Comment'].apply(normalize)

    stopwords = np.loadtxt(current_directory + "/data/stopwords.txt", dtype=np.str) # read in stopwords
    train['Tokenized'] = train['Tokenized'].apply(lambda comment: [word for word in comment if word not in stopwords])


