# Hangman Bot

```text
  +==========
  | /       |
  |/        O
  |       --+--
  |         |
  |        / \
  |
  +============
```

The objective of this competition is to create a bot that is the best at guessing words in a game of hangman.

## Scripts

Run the game an amount of times choosing random words for the bot to guess:

```console
python run_automated_word_game.py
```

Run the game with a user-promted word for the bot to guess:

```console
python run_user_prompted_word_game.py
```

## Competition Instructions

1. Add your bot class in bots.py.
2. Replace the following in run_automated_word_game.py and run_user_prompted_word_game.py with your bot:

  ```py
  player = bots.DumbBot()
  ```

3. Implement your bot to guess as many words as possible. You will be awarded points on how well your bot performs.
4. Along with your bot, submit 5 words that are difficult to guess. These words will be used against the best submitted bot, and you will be awarded points on how many the best bot cannot guess.

## Rules

1. There are 8 allowed mistakes.
2. The revealed word hides letters with `_`. E.g. in the word `r_s_`, 2 letters are hidden.
3. Chosen words are of length > 2.
4. Guessed letters must be a single valid character from `a` -> `z`.
5. The bot can only access the available letters, the revealed word, and the number of remaining mistakes. You cannot extend what the bot can see.
6. You cannot modify the game (unless there is a game-breaking bug that's found)

## Scoring

1. You get 10 points based on how many words your bot can guess out of 1000 random words. The random words will be the same for each participant, i.e. started at a fixed random seed for each participant. The value of the seed won't be revealed before the competition scoring, so you don't tune your bot to a specific set of words.
2. I will choose 10 "difficult to guess" hangman words. You get 1 point for each difficult word your bot can guess. The 10 words won't be revealed before the competition scoring.
3. Up to 5 bonus points are awarded for every submitted "difficult to guess" word that the best submitted bot **cannot** guess.
4. A bonus point for the fastest bot.
5. A bonus point for the most creative bot name.
6. A bonus point if any game-breaking bugs are found and fixed.
7. Bonus point(s) for readable and good-quality code.
8. You will lost points if your bot breaks the game.
