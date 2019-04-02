def create_enumerated_corpus(corpus):
    """Returns a dict of the enumerated vocabulary from the data, where the key is the word and value is a number."""
    return {word: number for number, word in enumerate(corpus)}


def test_create_corpus():
    assert create_enumerated_corpus(["figured", "apple"]) == {"figured": 0, "apple": 1}


def enumerate_comment(comment, dictionary):
    """Uses the enumerated corpus dictionary to enumerate each word in a tokenized comment within the data."""
    return list(map(lambda word: dictionary[word], comment))


def test_enumerate_comment():
    dictionary = create_enumerated_corpus(["figured", "apple"])
    assert enumerate_comment(["figured", "apple"], dictionary) == [0, 1]
