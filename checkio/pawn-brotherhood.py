files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def safe_pawns(pawns):
    result = 0
    for f, r in pawns:
        search_rank = str(int(r) - 1)
        index = files.index(f)
        result += (index > 0 and (files[index - 1] + search_rank in pawns)) or \
                  (index < 7 and (files[index + 1] + search_rank in pawns))
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
