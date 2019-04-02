import re


def escape_unicode(comment):
    """Returns a tokenized comment where the un-escaped unicode characters have been escaped."""
    return [word.encode('utf-8').decode('unicode_escape') if re.findall('\\\\\w+', word) != [] else word for word in
            comment]


def test_escape_a_acute():
    assert escape_unicode(['\\xe1']) == ['á']


def test_escape_a_umlaut():
    assert escape_unicode(['\\xe4']) == ['ä']


def test_escape_inverted_question_mark():
    assert escape_unicode(['\\xbf']) == ['¿']

def test_escape_sentence():
    assert escape_unicode(['Iam\\xbf trying to \\xe4figure out \\xe1 unicode']) == ['Iam¿ trying to äfigure out á unicode']


def replace_spaces(comment):
    """Replaces the unicode characters for whitespaces ad new lines with spaces."""
    pattern = '(\\\\xa0)|(\\\\n)|(\\\\xc2)'
    return [re.sub(pattern, " ", word) if re.findall(pattern, word) != [] else word for word in comment]


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
    assert replace_spaces(['test\\xc2\\xa0test\\ntest']) == ['test  test test']


def normalize(comment):
    """Returns the normalized comment.

    This is achieved by tokenizing and making the words lowercase, handling unicode issues and finally
    by stripping the remaining punctuation.

    Args:
        str: The original comment.

    Returns:
        list: A list of the normalized words in the comment.
    """
    tokenized = list(map(lambda word: word.lower(), comment.split(" ")))

    spaces_replaced_comment = replace_spaces(tokenized)
    cleaned_comment = escape_unicode(spaces_replaced_comment)

    return list(
        map(lambda word: word.translate(str.maketrans("", "", r"""[!"#$%&()*+,-./:;<=>?@[]^_`{|}~'\¿]""")),
            cleaned_comment))


def test_normalize_simple():
    assert normalize("HELLO YOU") == ["hello", "you"]


def test_normalize_newline():
    assert normalize("HELLO YOU! \\n") == ["hello", "you", " "]


def test_normalize_punctuation():
    assert normalize("HELLO YOU! &") == ["hello", "you", ""]


def test_normalize_double_backslash():
    assert normalize("HELLO YOU\\") == ["hello", "you"]
