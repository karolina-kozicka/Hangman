from game import Hangman
from helpers import load_words

words = load_words("hangman/slowa.txt")
game = Hangman(words)
game.play()
