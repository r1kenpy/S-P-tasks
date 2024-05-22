def count_words(data=None):
    words = {}
    if data is None:
        return words
    for word in data.split():
        word = word.strip(',.?!:;/"').lower()
        if word.isalpha():
            words[word] = words.setdefault(word, 0) + 1
    return words
