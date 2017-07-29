import re
from functools import reduce

VOWELS = "aeiouy"


def translate(phrase):
    phrase = re.sub(r'([^{0}\s])[{0}]'.format(VOWELS), r'\1', phrase)
    return reduce(lambda r, x: re.sub(r'([%s]){3}' % x, r'\1', r), VOWELS, phrase)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
