import re

def escape_unicode(sentence):
    """ Breaks up a sentence and searches each word for unicode errors, converting them to the proper format
    TODO \\xaO and \\n not being converted to should replace
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
