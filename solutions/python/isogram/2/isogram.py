def is_isogram(phrase):
    phrase = [char.lower() for char in list(phrase) if char != "-" and char != " "]
    return True if len(phrase) == len(set(phrase)) else False
