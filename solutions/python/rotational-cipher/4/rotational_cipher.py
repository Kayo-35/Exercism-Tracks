def rotate(text, key):
    conversion = ""

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")

            # Taking the letter ranges and converting
            shift_code = (ord(char) - base + key) % 26 + base
            conversion += chr(shift_code)
        else:
            # Preserving ponctuation chars, digits, etc
            conversion += char

    return conversion
