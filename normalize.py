import re

# TODO refactor to do and more tests with different unicode characters and when characters are near numbers

def escape_unicode(sentence):
    """ Breaks up a sentence and searches each word for unicode characters, converting them to their encoded form
    """
    return [word.encode('utf-8').decode('unicode_escape') if re.findall('\\\\\w+', word) != [] else word for word in
            sentence]


def test_escape_a_acute():
    assert escape_unicode(['\\xe1']) == ['á']


def test_escape_a_umlaut():
    assert escape_unicode(['\\xe4']) == ['ä']


def test_escape_inverted_question_mark():
    assert escape_unicode(['\\xbf']) == ['¿']

def replace_spaces(sentence):
    """ Replaces the unicode chcarcters for whitespaces ad new lines with spaces
    """
    pattern = '(\\\\xa0)|(\\\\n)|(\\\\xc2)'
    return [re.sub(pattern, " ", word) if re.findall(pattern, word) != [] else word for word in sentence]


def test_replace_whitespace():
    assert replace_spaces(['\\ntest']) == [' test']


def test_replace_beginning():
    assert replace_spaces(['\\xa0test test']) == [' test test']


def test_replace_middle():
    assert replace_spaces(['test\\xa0test']) == ['test test']


def test_replace_middle_twice():
    assert replace_spaces(['test\\xa0\\xa0test']) == ['test  test']


def test_replace_end():
    assert replace_spaces(['test\\xa0']) == ['test ']


def test_replace_space():
    assert replace_spaces(['test\\n test']) == ['test  test']


def test_replace_two_times():
    assert replace_spaces(['test\\n test\\n test']) == ['test  test  test']


def test_replace_different_unicode():
    assert replace_spaces(['test\\xc2\\xa0test\\n test']) == ['test  test  test']


def normalize(comment):
    """ Normailizes each comment, making the words lowercase, tokenizing them removing punctuation and escaping unicode characters
    """
    # splits comment into words and makes each word lowercase
    tokenized_comment = list(map(lambda word: word.lower(), comment.split(" ")))

    cleaned_comment = replace_spaces(tokenized_comment)
    cleaned_comment = escape_unicode(cleaned_comment)


    # strips punctuation & returns normalized comment
    return list(map(lambda word: word.translate(str.maketrans("", "", r"""[!"#$%&()*+,-./:;<=>?@[]^_`{|}~'\(\\\\\)¿]""")),
                    cleaned_comment))


def test_normalize_tokenize():
    assert normalize("HELLO YOU") == ["hello", "you"]


def test_normalize_unicode():
    assert normalize("HELLO YOU! \\n") == ["hello", "you", " "]


def test_normalize_punctuation():
    assert normalize("HELLO YOU! &") == ["hello", "you", ""]


def test_normalize_double_backslash():
    assert normalize("HELLO YOU\\") == ["hello", "you"]
