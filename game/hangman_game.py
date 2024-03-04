import logging

from game.words import available_words

ALLOWED_MISTAKES = 8


class HangmanGame:
    def __init__(self):
        self.available_letters = "abcdefghijklmnopqrstuvwxyz"
        self.remaining_allowed_mistakes = ALLOWED_MISTAKES
        self.word_to_guess = ""
        self.revealed_word = ""

    def set_word_to_guess(self, word_to_guess: str):
        """Choose a word that should be guessed."""
        if word_to_guess.lower() not in available_words:
            raise ValueError(f"Selected word '{word_to_guess}' is not in the list of valid words.")
        else:
            print("Word for the bot to guess is: ", word_to_guess)
            self.word_to_guess = word_to_guess.lower()
            self.revealed_word = "_" * len(word_to_guess)

    def make_guess(self, letter: str):
        """"""
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("Invalid letter.")
        if letter not in self.available_letters:
            raise ValueError("Letter has already been guessed.")

        self.available_letters = self.available_letters.replace(letter, "")
        if letter.lower() in self.word_to_guess:
            logging.info(
                "\U0001F389 Player guessed %s, which is in the word %d times!", letter, self.word_to_guess.count(letter)
            )
            self.revealed_word = "".join(
                [char if char == letter or char in self.revealed_word else "_" for char in self.word_to_guess]
            )
        else:
            self.remaining_allowed_mistakes -= 1
            logging.info(
                "\U0000274C Player guessed %s, which is not in the word. %d remaining mistakes.",
                letter,
                self.remaining_allowed_mistakes,
            )
        logging.info("Revealed word: %s", self.revealed_word)

    def is_word_guessed_correctly(self):
        return self.word_to_guess == self.revealed_word

    def has_lost(self):
        return self.remaining_allowed_mistakes < 0

    def reset(self):
        self.available_letters = "abcdefghijklmnopqrstuvwxyz"
        self.remaining_allowed_mistakes = ALLOWED_MISTAKES
        self.word_to_guess = ""
        self.revealed_word = ""
