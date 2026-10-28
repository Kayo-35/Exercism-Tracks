def response(hey_bob):
    """Returns Bob's responses to given conversations
    Parameters:
        hey_bob(str): A given string
    Returns:
        response(str): The response based on the conversation
    """

    hey_bob = hey_bob.strip()

    if len(hey_bob) == 0:
        return "Fine. Be that way!"
    if hey_bob[-1] == "?" and is_yelling(hey_bob):
        return "Calm down, I know what I'm doing!"
    if hey_bob[-1] == "?":
        return "Sure."
    if is_yelling(hey_bob):
        return "Whoa, chill out!"

    return "Whatever."


def is_yelling(phrase):
    phrase_letters = [
        letter for word in phrase.split() for letter in word if letter.isalpha()
    ]

    if len(phrase_letters) == 0:
        return False

    return all(letter.upper() == letter for letter in phrase_letters)


print(response("WHAT'S GOING ON?"))
