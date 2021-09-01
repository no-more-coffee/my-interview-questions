import re


def is_stressful(subj):
    """

        recoognise stressful subject

    """
    if subj.isupper():
        return True

    if subj.endswith('!!!'):
        return True

    for word in subj.lower().split():
        for red_word in ['help', 'asap', 'urgent']:
            if re.search('+\W*'.join(red_word), word) is not None:
                return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("I neeed heeelp") == True
    assert is_stressful("I neeed he1lp") == False
    print('Done! Go Check it!')
