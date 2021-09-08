import pygame
import time

ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

TIME_BETWEEN = 0.5  # Time between sounds
PATH = "morse_code_audio/"


def verify(string):
    keys = list(ENGLISH_TO_MORSE.keys())
    for char in string:
        if char not in keys and char != " ":
            print(f"The character {char} cannot be translated.")
            raise SystemExit


def main():
    print("### English to Morse Code Audio Converter ###")
    print("Enter your message in English: ")
    message = input("> ").upper()
    verify(message)

    pygame.init()

    for char in message:
        if char == " ":
            print(" " * 3, end=" ")  # Separate words clearly
            time.sleep(7 * TIME_BETWEEN)
        else:
            print(ENGLISH_TO_MORSE[char.upper()], end=" ")
            pygame.mixer.music.load(PATH + char + '_morse_code.ogg')  # You will need these sound files
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play()
            time.sleep(3 * TIME_BETWEEN)


if __name__ == "__main__":
    main()