def rank_corpus(corpus):
    """Returns a dictionary of words where the key is the word and the value is frequency ranking. The most common word
    will have the value 1.

    Args:
        list: The normalized vocabulary from the data set

    Returns:
        dict: A dictionary of the corpus vocabulary

    """
    return {word: number for number, word in enumerate(corpus)}


def test_create_corpus():
    assert rank_corpus(["figured", "apple"]) == {"figured": 0, "apple": 1}


def enumerate_comment(comment, dictionary):
    """Uses the enumerated corpus dictionary to enumerate each word in a tokenized comment within the data."""
    return list(map(lambda word: dictionary[word], comment))


def test_enumerate_comment():
    dictionary = rank_corpus(["figured", "apple"])
    assert enumerate_comment(["figured", "apple"], dictionary) == [0, 1]


def count_words(corpus):
    """Returns a sorted list of tuples of word, count pairs. The order is reversed. This means the highest count will
    be the final entry.
    """
    word_frequency = dict([(word, corpus.count(word)) for word in set(corpus)])
    ascending_order_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1])
    return ascending_order_word_frequency

def test_counted_words():
    assert set(count_words(["apple", "apple", "banana", "acorn"])) ==  set([('banana', 1), ('acorn', 1), ('apple', 2)])

def test_sort_counted_words():
    assert count_words(["strawberry", "apple", "apple", "banana", "acorn"])[-1] ==  ('apple', 2)
#     Ordering of words with same count changes each execution
#    assert count_words(["strawberry", "apple", "apple", "banana", "acorn"])[0] == ('apple', 2)



