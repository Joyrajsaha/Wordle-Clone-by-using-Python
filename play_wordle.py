from typing import List
from letter_position import LetterPosition
from wordle import Wordle
from colorama import Fore
import random


def main():
    word_set = load_word_set("data/words.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)
    print(secret)
    print('Rules of the game: \n1. Each guess must be a valid five-letter word and should be in capital letters. ')
    print('2. If the letter color is in green that means the letter is in the word and in the correct spot..')
    print('3. If the letter color is in red that means the letter is in the word but in the wrong spot..')
    print('4. If the letter color is normal that means The letter is not in the word in any spot..')

    while wordle.can_attempt:
        x = input("\nType your guess: ")

        if len(x) != wordle.WORD_LENGTH:
            print(
                Fore.RED
                + f"Word must be {wordle.WORD_LENGTH} characters long!"
                + Fore.RESET
            )
            continue

        if not x in word_set:
            print(
                Fore.RED
                + f"{x} is not a valid word!"
                + Fore.RESET
            )
            continue

        wordle.attempt(x)
        display_results(wordle)

    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("You failed to solve the puzzle!")
        print(f"The secret word was: {wordle.secret}")


def display_results(wordle: Wordle):
    print("\nYour results so far...")
    print(f"You have {wordle.remaining_attempts} attempts remaining.\n")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    draw_border_around(lines)


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


def convert_result_to_color(result: List[LetterPosition]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.BLUE
        else:
            color = Fore.WHITE
        colored_letter = color + letter.ch + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)


def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    space = " " * pad

    for line in lines:
        print(" " + space + line + space + " ")


if __name__ == "__main__":
    main()
