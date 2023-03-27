from random import choice
from os import system
from time import sleep
from constants import words_list, display_texts, should_play_responses

class game:
    def __init__(self, words_list:str) -> None:
        self.play:bool = False
        self.random_word:str = ''
        self.player_lives:int = 0
        self.player_letter_guess_list:list = []

    def prompt_player_guess(self) -> None:
        player_guess = input(display_texts['user_guess']).upper()        
        if player_guess == self.random_word: # Player guessed word
            self.player_letter_guess_list = player_guess.split(',')
            self.clear_screen()

        elif len(player_guess) == 1 and player_guess in self.random_word: # Player guessed letter in word 
            self.clear_screen()   
            indexes_of_guess_in_random_word = [idx for idx, value in enumerate(self.random_word) if value == player_guess]
            for idx in indexes_of_guess_in_random_word:
                self.player_letter_guess_list[idx] = player_guess
                
        else: # Player guessed incorrectly
            self.clear_screen()
            self.player_lives -= 1

    def should_play(self, text:str = display_texts['play_game'] ) -> bool:
        if input(text).capitalize() in should_play_responses:
            return True
        else:
            return False

    def get_player_letter_guesses(self) -> None:
       return ''.join(self.player_letter_guess_list).capitalize()

    def quit_game(self) -> None:
        self.clear_screen()
        self.play = False
        print(display_texts['quit_game'])
        self.clear_screen(2)

    def win_game(self) -> None:
        if self.should_play(display_texts['play_again']):
            self.set_game()
        else:
            self.quit_game()

    def set_game(self) -> None:
        self.clear_screen()
        self.random_word = choice(words_list).upper()
        self.player_lives = len(self.random_word)
        self.player_letter_guess_list = ['_'] * len(self.random_word)
        print(display_texts['ready_to_play'])
        print(f'The word im thinking of is {len(self.random_word)} letters long')
        self.clear_screen(3)

    def clear_screen(self, time=0):
        sleep(time)
        system('clear')

    def play_hangman(self) -> None:
        self.play = self.should_play()
        self.set_game()
        
        while self.play:

            if not self.player_lives:
                print(display_texts['out_of_lives'])
                self.clear_screen(2)
                if self.should_play(display_texts['play_again']):
                    self.set_game()
                else:
                    self.quit_game()
            
            while self.player_lives:
                self.clear_screen()
                print(f'{self.get_player_letter_guesses()}  lives: {self.player_lives}\n')

                if self.get_player_letter_guesses().upper() == self.random_word:
                    print(f"{display_texts['player_wins']}'{self.random_word.capitalize()}'")
                    self.clear_screen(2)
                    self.win_game()
                    break
                else:                        
                    self.prompt_player_guess()
            
if __name__ == "__main__":
    game(words_list).play_hangman()
