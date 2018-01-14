def checkio(number):
    res = []
    for i in range(9, 1, -1):
        while not number % i:
            res.append(i)
            number /= i
    if not res or number > 1:
        return 0
    return int(''.join(map(str, sorted(res))))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"




def checkio(data):
    
    fs = []
    for p in range(9, 1, -1):
        while bool(data) and ((data%p) == 0):
            fs += [str(p)]
            data /= p
    return int(''.join(sorted(fs)), 10) if (data == 1) else 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(5) == 5, "5th example"
