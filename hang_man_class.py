from random import choice
from os import path

from constants import WORDS_LIST, SHOULD_PLAY_RESPONSES, DISPLAY_TEXTS
from helpers import colorGreen, colorYellow, read_from_file, underline, clear_terminal, write_to_file

if not path.exists("./score_board.json"): write_to_file("./score_board.json", {"top_score":{"score":0, "player":""}})
score_board = read_from_file("./score_board.json")

class Hangman:

    
    def __init__(self, player: str) -> None:
        self.__word: str = choice(WORDS_LIST).lower()
        self.__points: int = 0
        self.__player_guess: str = None
        self.__letters_guessed: list[str] = ["_"] * len(self.__word)
        self.__top_player: str = score_board["top_score"]["player"] 
        self.__top_score: int = score_board["top_score"]["score"]
        self.__player: dict = {
            "name": player.capitalize(),
            "score": score_board[player] if player in score_board else 0,
            "lives": len(self.__word),
            "is_new_player": player.capitalize() not in score_board
        }

    def __display_high_score(self) -> None: 
        print(f"{underline(self.__top_player or 'Top_Score')}: {colorYellow(self.__top_score or 'None')} | {underline(self.__player['name'])}: {colorYellow(self.__player['score'])}\n")
    
    def __display_game_data(self) -> None: 
        print(f"Points: {colorGreen(self.__points)} Word: {colorGreen(' '.join(self.__letters_guessed).capitalize())} Lives: {colorGreen(self.__player['lives'])}\n")

    def __update_score_board(self) -> None:
        if self.__player["is_new_player"] or self.__points > self.__player["score"]:
            score_board[self.__player["name"]] = self.__points
            self.__player["score"] = self.__points

        if self.__points > self.__top_score:
            score_board["top_score"]["score"] = self.__points
            score_board["top_score"]["player"] = self.__player["name"]

            self.__top_score = score_board["top_score"]["score"]
            self.__top_player = score_board["top_score"]["player"]

        write_to_file("./score_board.json", score_board)

    def __update_letters_guessed(self):
        if self.__player_guess == self.__word:
            self.__letters_guessed = self.__player_guess.split()
        else:
            indices_of_guess_in_random_word = [index for index, value in enumerate(self.__word) if value == self.__player_guess]
            for index in indices_of_guess_in_random_word:
                self.__letters_guessed[index] = self.__player_guess
                    
    def __update_game(self) -> None:
        clear_terminal()
        self.__update_letters_guessed()
        self.__update_score_board()
        self.__display_high_score()
        self.__display_game_data()

    def reset_word(self) -> str:
        self.__word = choice(WORDS_LIST).lower()
        self.__letters_guessed: list[str] = ["_"] * len(self.__word)
        return self.__word

    def update_user_guess(self, guess:str) -> None:
        self.__player_guess = guess
        self.__update_letters_guessed()

    def update_player_points(self, points:int) -> None:
        self.__points = points
        self.__update_score_board()

    def update_player_lives(self, lives:int) -> None:
        self.__player["lives"] = lives

    def get_state(self, key: str = None) -> str | dict | int | list: 
        state = {
            "word": self.__word, 
            "user_guess": self.__player_guess, 
            "guesses": self.__letters_guessed, 
            "high_score":{
                "player": self.__top_player,
                "score": self.__top_score
            },
            "player": self.__player,
            "points": self.__points
        }
        if key:
            return state[key]
        return state

    def play_game(self) -> None:

        self.__update_game()

        if str(self.__player_guess).lower() != "quit":

            if not self.__player["lives"]:
                print(DISPLAY_TEXTS["out_of_lives"])
                clear_terminal(2)

            elif self.__player_guess == self.__word or ''.join(self.__letters_guessed).lower() == self.__word:
                print(DISPLAY_TEXTS["player_wins"])
                clear_terminal(2)

                current_points = self.__points + self.__player["lives"]
                next_game = Hangman(self.__player["name"])
                next_game.__points = current_points
                next_game.play_game()

            else:
                if not self.__player_guess or self.__player_guess not in self.__word:
                    self.__player_guess = input(DISPLAY_TEXTS["user_guess"]).lower()
                    self.play_game()
                else:
                    self.__player["lives"] -= 1
                    self.__player_guess = None
                    clear_terminal()
                    self.play_game()
        else:
            print(DISPLAY_TEXTS["quit_game"])
            clear_terminal(2)

            
if __name__ == "__main__":

    clear_terminal()

    if input(DISPLAY_TEXTS["should_play_game"]).capitalize() in SHOULD_PLAY_RESPONSES:
        clear_terminal()
        player = input(DISPLAY_TEXTS["get_player_name"]).capitalize()
        clear_terminal()

        print(f"Welcome back, {player}") if player in score_board else print(f"Let's play, {player}")
        clear_terminal(2)

        print(DISPLAY_TEXTS["ready_to_play"])
        clear_terminal(4.5)

        Hangman(player).play_game()

    else:
        print(DISPLAY_TEXTS["quit_game"])
        clear_terminal(2)
