def get_all(text):
    for i in range(len(text)):
        for j in range(i, len(text) + 1):
            text_right = text[i:j]
            if text_right == text_right[::-1]:
                yield text_right


def longest_palindromic(text):
    res = get_all(text)
    return max(res, key=len)


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
