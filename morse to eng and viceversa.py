ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# Generate MORSE_TO_ENGLISH from ENGLISH_TO_MORSE
MORSE_TO_ENGLISH = {}
for key, value in ENGLISH_TO_MORSE.items():
    MORSE_TO_ENGLISH[value] = key


def english_to_morse(message):
    morse = []  # Will contain Morse versions of letters
    for char in message:
        if char in ENGLISH_TO_MORSE:
            morse.append(ENGLISH_TO_MORSE[char])
    return " ".join(morse)


def morse_to_english(message):
    message = message.split(" ")
    english = []  # Will contain English versions of letters
    for code in message:
        if code in MORSE_TO_ENGLISH:
            english.append(MORSE_TO_ENGLISH[code])
    return " ".join(english)


def main():
    while True:
        response = input("Convert Morse to English (1) or Convert English to Morse (2)? ").upper()
        if response == "1" or response == "2":
            break

    if response == "1":
        print("Enter Morse code (with a space after each code): ")
        morse = input("> ")
        english = morse_to_english(morse)
        print("### English version ###")
        print(english)

    elif response == "2":
        print("Enter English text: ")
        english = input("> ").upper()
        morse = english_to_morse(english)
        print("### Morse Code version ###")
        print(morse)


if __name__ == "__main__":
    main()