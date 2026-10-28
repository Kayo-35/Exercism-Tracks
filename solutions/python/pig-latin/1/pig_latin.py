import stat
from turtle import st


def translate(text: str):
    """Translates english to pig-latin
    Parameters:
        text(str): The text to be translated
    Returns:
        translation(str): The translation obtained
    Notes:
        For more on pig-latin: https://en.wikipedia.org/wiki/Pig_latin
    """
    words_in_text = text.lower().split()

    def translate_word(word: str):
        vowels = ["a", "e", "i", "o", "u"]
        index_of_vowels = [word.index(vowel) for vowel in vowels if vowel in word]
        index_of_vowels.sort()

        if word.startswith(("xr", "yt")) or word[0] in vowels:
            return word + "ay"

        if (
            word[0] != "y"
            and "y" in word
            and all(letter not in vowels for letter in word[0 : word.index("y")])
        ):
            if len(word) == 2:
                return "y" + word[0 : word.index("y")] + "ay"
            return word[word.index("y") :] + word[0 : word.index("y")] + "ay"

        if "qu" in word and not word[word.index("qu") - 1] in vowels:
            if word.startswith("qu"):
                return word.removeprefix("qu") + "qu" + "ay"
            return (
                word[word.index("qu") + 2 :] + word[0 : word.index("qu")] + "qu" + "ay"
            )

        return word[index_of_vowels[0] :] + word[0 : index_of_vowels[0]] + "ay"

    words_in_text = [translate_word(word) for word in words_in_text]

    return " ".join(words_in_text)
