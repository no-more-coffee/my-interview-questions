def checkio(words):
    counter = 0
    for i in words.split(' '):
        nums = tuple(j for j in i if j.isnumeric())
        if nums:
            counter = 0
            continue
        counter += 1
        if counter == 3:
            return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert checkio("one two 3 four five 6 seven eight 9 ten eleven 12 ") == False, "their"
