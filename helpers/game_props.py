from random import choice

from utils.constants import WORDS_LIST

class Game:
    word:str
    points:int
    lives:int
    player_guess:str|None
    letters_guessed_lst:list[str]

    def __init__(self):
        self.word = choice(WORDS_LIST).lower()
        self.points = 0
        self.lives = 6
        self.player_guess = None
        self.letters_guessed_lst = ["_"] * len(self.word)

    def reset(self) -> None:
        self.word = choice(WORDS_LIST).lower()
        self.lives = 6
        self.player_guess = None
        self.letters_guessed_lst = ["_"] * len(self.word)
        
    def update_points(self) -> None:
        self.points += self.lives

    def decrement_lives(self) -> None:
        self.lives -= 1

    def set_guess(self, guess:str|None = None) -> None:
        self.player_guess = guess.lower() if guess else guess
        self.update_letters_guessed()

    def word_guessed(self) -> bool:
        return self.player_guess == self.word or self.format_letters_guessed() == self.word
    
    def guess_in_word(self) -> bool:
        return self.player_guess in self.word
    
    def format_letters_guessed(self, format_option: str = '') -> str:
        return format_option.join(self.letters_guessed_lst)
    
    def update_letters_guessed(self) -> None:
        if self.player_guess == self.word:
            self.letters_guessed_lst = self.player_guess.split()
        else:
            indices_of_guess_in_random_word = [index for index, value in enumerate(self.word) if value == self.player_guess]
            for index in indices_of_guess_in_random_word:
                self.letters_guessed_lst[index] = self.player_guess