def is_isogram(phrase):
    letters = list("abcdefghijklmnopqrstuvwxyz")

    phrase.split()
    phrase = [word.lower() for word in phrase]

    amount_of_appearances = [phrase.count(char) for char in phrase if char in letters]

    if sum(amount_of_appearances) == len(amount_of_appearances):
        return True
    return False


print(is_isogram("Emily Jung Schwartzkopf"))
