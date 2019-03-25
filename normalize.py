import re

def escape_unicode(sentence):
    """ Breaks up a sentence and searches each word for unicode errors, converting them to the proper format
    TODO \\xaO and \\n not being converted to should replace - this still needs improving
    """
    return [word.encode('utf-8').decode('unicode_escape') if re.findall('\\\\\w+', word) != [] else word for word in sentence]


def test_escape_whitespace():
    assert escape_unicode(['\\ntest']) == ['\ntest']


def test_escape_hex():
    assert escape_unicode(['\\xa0']) == ['\xa0']


def test_escape_beginning():
    assert escape_unicode(['\\xa0test test']) == ['\xa0test test']


def test_escape_middle():
    assert escape_unicode(['test\\xa0test']) == ['test\xa0test']


def test_escape_middle_twice():
    assert escape_unicode(['test\\xa0\\xa0test']) == ['test\xa0\xa0test']


def test_escape_end():
    assert escape_unicode(['test\\xa0']) == ['test\xa0']


def test_escape_space():
    assert escape_unicode(['test\\n test']) == ['test\n test']


def test_escape_two_times():
    assert escape_unicode(['test\\n test\\n test']) == ['test\n test\n test']


def normalize(comment):
    """ Normailizes each comment, making the words lowercase, tokenizing them removing punctuation and escaping unicode characters

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
