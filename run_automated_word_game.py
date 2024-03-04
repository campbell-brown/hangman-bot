"""Generates a random word from the list of available words and gets the bot to guess it."""

import logging
import random

import game.bots as bots
from game.hangman_game import HangmanGame
from game.words import available_words

TOTAL_ATTEMPTS = 100

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    hangman_game = HangmanGame()
    player = bots.DumbBot()

    wins = 0
    attempts = 0
    while attempts < TOTAL_ATTEMPTS:
        word_to_guess = random.choice(available_words)
        print(word_to_guess in available_words)
        hangman_game.set_word_to_guess(word_to_guess)

        while not hangman_game.is_word_guessed_correctly() and not hangman_game.has_lost():
            letter = player.choose_letter(
                hangman_game.available_letters, hangman_game.revealed_word, hangman_game.remaining_allowed_mistakes
            )
            hangman_game.make_guess(letter)

        if hangman_game.is_word_guessed_correctly():
            logging.info("Bot has guessed the word correctly!")
            wins += 1
        else:
            assert hangman_game.has_lost()
            logging.warning("Bot has lost!")

        hangman_game.reset()
        player.reset()
        attempts += 1

    logging.info("Bot won %d/%d games.", wins, attempts)
