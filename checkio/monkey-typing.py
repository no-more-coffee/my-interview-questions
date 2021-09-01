def count_words(text, words):
    return sum(x for x in words if x in text.lower())
