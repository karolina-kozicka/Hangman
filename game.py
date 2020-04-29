import random

from draw import hangman_drawings


class Hangman:
    INITIAL_HP = 7

    def __init__(self, list_of_words):
        self.list_of_words = list_of_words
        self.letters = []
        self.hp = self.INITIAL_HP

    def play(self):
        self.choose_word()
        self.draw_board()
        while True:
            letter = self.provide_letter()
            self.check_letter(letter)
            self.draw_board()
            self.draw_man()
            print(f"Sprawdzone litery: {self.letters}\n")

            if self.hp == 0:
                print(f"Przegrałeś. Poszukiwane słowo to: {self.word}")
                break
            if "_" not in self.board:
                print("Wygrałeś!")
                break

    def choose_word(self):
        self.word = random.choice(self.list_of_words).upper()

    def draw_board(self):
        self.board = []
        for letter in self.word:
            if letter in self.letters:
                self.board.append(letter)
            else:
                self.board.append("_")
        print(" ".join(self.board))

    def check_letter(self, letter):
        self.letters.append(letter)
        if letter not in self.word:
            self.hp -= 1

    def provide_letter(self):
        letter = input("Wprowadź literę: ").upper()
        while True:
            if not letter.isalpha() or len(letter) != 1:
                letter = input(f"Proszę wprowadź JEDNĄ LITERERĘ: ").upper()
            elif letter in self.letters:
                letter = input(
                    f"'{letter}' już sprawdzałeś! Proszę wprowadź inną literę: "
                ).upper()
            else:
                return letter

    def draw_man(self):
        if self.hp != self.INITIAL_HP:
            print(hangman_drawings[self.hp])
