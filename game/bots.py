import random

from game.words import available_words


class Bot:
    """A bot that can guess a word."""

    def reset(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def choose_letter(self, available_letters: str, revealed_word: str, remaining_allowed_mistakes: int) -> str:
        """Choose a letter to guess.

        Args:
            available_letters: A string containing the letters that have not been guessed yet.
            revealed_word: A string containing the word with the guessed letters revealed.
                           Letters are hidden with underscores `_`.
            remaining_allowed_mistakes: The number of mistakes the player can still make.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class DumbBot(Bot):
    """A dumb bot that guesses letters at random from the available letters."""

    def __init__(self):
        pass

    def reset(self):
        pass

    def choose_letter(self, available_letters: str, revealed_word: str, remaining_allowed_mistakes: int) -> str:
        return random.choice(available_letters)


# TODO: Add your bot here!
