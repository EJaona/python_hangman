from random import choice
from os import path
from constants import words_list, display_texts, should_play_responses
from helpers import colorGreen, colorYellow, read_from_file, underline, clear_terminal, write_to_file

if not path.exists('./score_board.json'):
    write_to_file('./score_board.json', {"top_score":{"score":0, "player":''}})

score_board = read_from_file('./score_board.json')

class Hang_man:
    def __init__(self, player:str) -> None:
        self.__word:str = choice(words_list).lower()
        self.__points:int = 0
        self.__user_guess:None|str = None
        self.__player_letter_guessed:list[str] = ["_"] * len(self.__word)

        self.__top_player:str = score_board['top_score']['player'] 
        self.__top_score:int = score_board['top_score']['score']

        self.__current_player:dict = {}
        self.__current_player["name"]:str = player
        self.__current_player["score"]:int = score_board[player] if player in score_board else 0
        self.__current_player["lives"]:int = len(self.__word)

    def __display_high_score(self): print(f"{ underline(self.__top_player or 'Top_Score') }: { colorYellow(self.__top_score or 'None') } | { underline(self.__current_player['name']) }: { colorYellow(self.__current_player['score']) }\n")
    
    def __display_game_data(self): print(f"Points: { colorGreen(self.__points) } Word: { colorGreen(' '.join(self.__player_letter_guessed).capitalize()) } Lives: { colorGreen(self.__current_player['lives']) }\n")

    def __update_score_board(self):

        if not self.__current_player['name'] in score_board or self.__points > self.__current_player["score"]:
            score_board[self.__current_player['name']] = self.__points
            self.__current_player["score"] = self.__points

        if self.__points > self.__top_score:
            score_board["top_score"]["score"] = self.__points
            score_board["top_score"]["player"] = self.__current_player['name']

            self.__top_score = score_board["top_score"]["score"]
            self.__top_player = score_board["top_score"]["player"]

        write_to_file('./score_board.json', score_board)
            
    def __update_game(self) -> None:

        if self.__user_guess == self.__word:
            self.__player_letter_guessed = self.__user_guess.split()
            clear_terminal()

        else:
            clear_terminal()   
            indices_of_guess_in_random_word = [i for i, value in enumerate(self.__word) if value == self.__user_guess]
            for i in indices_of_guess_in_random_word:
                self.__player_letter_guessed[i] = self.__user_guess
   
        self.__update_score_board()
        self.__display_high_score()
        self.__display_game_data()        

    def play_game(self) -> None:

        self.__update_game()

        if str(self.__user_guess).lower() != 'quit':

            if not self.__current_player['lives']:
                print(display_texts['out_of_lives'])
                clear_terminal(2)

            elif self.__user_guess == self.__word or ''.join(self.__player_letter_guessed).lower() == self.__word:
                print(display_texts['player_wins'])
                clear_terminal(2)

                current_points = self.__points + self.__current_player['lives']
                next_game = Hang_man(self.__current_player['name'])
                next_game.__points = current_points
                next_game.play_game()

            else:
                if not self.__user_guess or not self.__user_guess in self.__word:
                    self.__user_guess = input(display_texts['user_guess']).lower()
                    self.play_game()
                else:
                    self.__current_player['lives'] -= 1
                    self.__user_guess = None
                    clear_terminal()
                    self.play_game()
        else:
            print(display_texts['quit_game'])
            clear_terminal(2)
            
if __name__ == "__main__":
    clear_terminal()

    if input(display_texts['should_play_game']).capitalize() in should_play_responses:
        clear_terminal()
        player = input(display_texts['get_player_name']).capitalize()
        clear_terminal()

        print(f'Welcome back, { player }') if player in score_board else print(f"Let's play, { player }")
        clear_terminal(2)

        print(display_texts['ready_to_play'])
        clear_terminal(4.5)

        Hang_man(player).play_game()

    else:
        print(display_texts['quit_game'])
        clear_terminal(2)
