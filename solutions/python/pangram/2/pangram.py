def is_pangram(sentence: str):
    sentence = sentence.lower()
    alphabet_chars = "abcdefghijklmnopqrstuvwxyz"

    # Checking if each letter in on the text at least once
    for letter in alphabet_chars:
        if letter not in sentence:
            return False

    return True
