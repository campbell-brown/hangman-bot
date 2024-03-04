"""Prompts the user to choose a word and gets the bot to guess it."""
import logging
import sys

import game.bots as bots
from game.hangman_game import HangmanGame
from game.words import available_words


def setup(game: HangmanGame, player) -> None:
    game.reset()
    player.reset()
    try:
        while True:
            word = input("Please enter a word for the bot to guess: ")
            if word.lower() in available_words:
                word_to_guess = word.lower()
                break
            print("That word is not in the list of valid words. Please try again.")
        game.set_word_to_guess(word_to_guess)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    hangman_game = HangmanGame()
    player = bots.DumbBot()

    setup(hangman_game, player)

    while True:
        letter = player.choose_letter(
            hangman_game.available_letters, hangman_game.revealed_word, hangman_game.remaining_allowed_mistakes
        )
        hangman_game.make_guess(letter)

        if hangman_game.is_word_guessed_correctly():
            logging.info("Bot has guessed the word correctly!")
            setup(hangman_game, player)
            continue

        if hangman_game.has_lost():
            logging.warning("Bot has lost!")
            setup(hangman_game, player)
            continue
