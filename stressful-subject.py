from functools import reduce

red_words = ("help", "asap", "urgent")


def is_stressful(subj):
    """
        recoognise stressful subject
    """
    if subj.endswith('!!!'):
        return True

    subj = ''.join(filter(lambda x: x.isalpha(), subj))
    if subj.isupper():
        return True

    subj = ''.join(reduce((lambda res, x: res if res.endswith(x) else (res + x)), subj.lower()))
    for i in red_words:
        if i in subj:
            return True

    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
