def is_pangram(sentence: str):
    sentence = sentence.lower()
    alphabet_chars = "abcdefghijklmnopqrstuvwxyz"

    return all(letter in sentence for letter in alphabet_chars)
