def convert(number):
    sound_made = ""

    if number % 3 == 0:
        sound_made += "Pling"
    if number % 5 == 0:
        sound_made += "Plang"
    if number % 7 == 0:
        sound_made += "Plong"

    return sound_made if sound_made else str(number)
