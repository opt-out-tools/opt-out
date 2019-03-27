
def enumerate_corpus(corpus):
    """ Used to create a look up table for the vocabulary for later conversion back to the original sentence
    """
    return {word: number for number, word in enumerate(corpus)}


def test_enumerate_corpus():
    assert enumerate_corpus(["figured", "apple"]) == {"figured": 0, "apple": 1}


def enumerate_comment(comment, dictionary):
    """ Enumerate the comments in order to pre-process them (padding)
    """

    return list(map(lambda word : dictionary[word], comment))

def test_enumerate_comment():
    dictionary = enumerate_corpus(["figured", "apple"])

    assert enumerate_comment(["figured", "apple"], dictionary) == [0, 1]