def is_isogram(phrase):
    phrase = [char.lower() for char in list(phrase) if char not in ["-", " "]]
    return True if len(phrase) == len(set(phrase)) else False
