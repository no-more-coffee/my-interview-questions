brackets = {
    '(': ')',
    '{': '}',
    '[': ']',
}


def checkio(expression):
    stack = []
    for i in expression:
        keys = brackets.keys()
        values = brackets.values()
        if i in keys:
            stack.append(i)
        if i in values:
            try:
                if i != brackets[stack.pop()]:
                    return False
            except IndexError:
                return False
    return stack == []


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("(((1+(1+1))))]") == False
