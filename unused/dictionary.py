def rank_corpus(corpus):
    """Returns a dictionary of words where the key is the word and the value is frequency ranking. The most common word
    will have the value 1.

    Args:
        list: The normalized vocabulary from the data set

    Returns:
        dict: A dictionary of the corpus vocabulary

    """
    return {word: number for word, number in rank(corpus)}


def test_create_corpus():
    assert rank_corpus(["figured", "apple"]) == {"figured": 1, "apple": 1}


def enumerate_comment(comment, dictionary):
    """Uses the enumerated corpus dictionary to enumerate each word in a tokenized comment within the data."""
    return list(map(lambda word: dictionary[word], comment))


def test_enumerate_comment():
    dictionary = rank_corpus(["figured", "apple"])
    assert enumerate_comment(["figured", "apple"], dictionary) == [1, 1]


def count_words(corpus):
    """Returns a sorted list of tuples of word, count pairs. The order is reversed. This means the highest count will
    be the first entry.
    """
    return sorted([(word, corpus.count(word)) for word in set(corpus)], key=lambda t: t[1], reverse=True)


def test_counted_words():
    assert set(count_words(["apple", "apple", "banana", "acorn"])) == set([('banana', 1), ('acorn', 1), ('apple', 2)])


def test_sort_counted_words():
    assert count_words(["strawberry", "apple", "apple", "banana", "acorn"])[0] == ('apple', 2)


#     Ordering of words with same count changes each execution
#    assert count_words(["strawberry", "apple", "apple", "banana", "acorn"])[-1] == ('strawberry', 2)


def rank(corpus):
    word_frequencies = count_words(corpus)

    ranking = []
    i = 1
    before = 0
    for word, frequency in word_frequencies:

        if (frequency == before):
            ranking.append((word, j))
            continue
        else:
            ranking.append((word, i))

        before = frequency
        j = i
        i += 1
    return ranking


def test_rank_basic():
    corpus = ["apple", "apple", "apple", "banana", "acorn"]
    assert rank(corpus)[0] == ('apple', 1)
    assert set(rank(corpus)) == set([('apple', 1), ('acorn', 2), ('banana', 2)])


def test_rank_longer():
    corpus = ["apple", "apple", "apple", "banana", "acorn", "pear", "pear", "pear", "pear"]
    assert rank(corpus)[0] == ('pear', 1)
    assert set(rank(corpus)) == set([('pear', 1), ('apple', 2), ('acorn', 3), ('banana', 3)])


def decode_review(text, word_index):
        reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
        return ' '.join([reverse_word_index.get(i, '?') for i in text])
