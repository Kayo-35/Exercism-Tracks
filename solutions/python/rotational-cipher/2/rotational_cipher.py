def make_translation_table(letters_set, key):
    translation_chars = []

    for index, letter in enumerate(letters_set):
        if index + key > 25:
            remaining_rotation = (index + key) - 25
            # -1 because the counting starts on 0
            translation_chars.append(letters_set[remaining_rotation - 1])
        else:
            translation_chars.append(letters_set[index + key])

    return translation_chars


def rotate(text, key):
    letters = list("abcdefghijklmnopqrstuvwxyz")
    uppercase_letters = [letter.upper() for letter in letters]

    lowercase_char_translation = make_translation_table(letters, key)
    uppercase_char_translation = make_translation_table(uppercase_letters, key)

    translation_table_lowercase = str.maketrans(
        "".join(letters), "".join(lowercase_char_translation)
    )
    translation_table_uppercase = str.maketrans(
        "".join(uppercase_letters), "".join(uppercase_char_translation)
    )

    translated_chars = []

    for char in text:
        if char == char.upper():
            translated_chars.append(char.translate(translation_table_uppercase))
        else:
            translated_chars.append(char.translate(translation_table_lowercase))

    final_text = "".join(translated_chars)

    return final_text
