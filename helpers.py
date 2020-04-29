def load_words(path):
    with open(path, "r") as text_words:
        words = text_words.readlines()
    return [word.strip() for word in words]
