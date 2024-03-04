import nltk

MIN_WORD_LEN = 3

print("Downloading valid words for the game...")
nltk.download("words")
available_words = [word.lower() for word in nltk.corpus.words.words() if len(word) >= MIN_WORD_LEN]
print("Finished downloading valid words.")
print(f"{len(available_words)} words available for the game.")
