from random import choice

from utils.constants import WORDS_LIST, SHOULD_PLAY_RESPONSES, DISPLAY_TEXTS
from utils.fs import create_file, write_to_file, clear_terminal, colorGreen, colorYellow, underline

scoreboard_path = "score_board.json"
scoreboard = create_file(scoreboard_path, {"top":{"score":0, "player":""}, "scores":{}})

class Hangman:


    def __init__(self, player_name:str) -> None:
        player_name = player_name.capitalize()

        self.__word: str = choice(WORDS_LIST).lower()
        self.__points: int = 0

        self.__player_guess: str = None
        self.__letters_guessed_list: list[str] = ["_"] * len(self.__word)

        self.__top:dict = scoreboard["top"]

        self.__player: dict[str, int, int, bool] = {
            "name": player_name,
            "score": scoreboard["scores"][player_name] if player_name in scoreboard["scores"] else 0,
            "lives": 6,
            "is_new_player": player_name not in scoreboard["scores"]
        }
    
    def __display_high_score(self) -> None: 
        print(f"{underline(self.__top['player'] or 'Top_Score')}: {colorYellow(self.__top['score'] or 'None')} | {underline(self.__player['name'])}: {colorYellow(self.__points)}\n")
    
    def __display_game_data(self) -> None: 
        print(f"Points: {colorGreen(self.__points)} Word: {colorGreen(' '.join(self.__letters_guessed_list).capitalize())} Lives: {colorGreen(self.__player['lives'])}\n")

    def __update_scoreboard(self) -> None:
        if self.__player["is_new_player"] or self.__points > self.__player["score"]:
            scoreboard["scores"][self.__player["name"]], self.__player["score"]  = self.__points

        if self.__points > self.__top["score"]:
            scoreboard["top"]["score"] = self.__points
            scoreboard["top"]["player"] = self.__player["name"]
            self.__top = scoreboard["top"]

        write_to_file(scoreboard_path, scoreboard)

    def __update_letters_guessed_list(self):
        if self.__player_guess == self.__word:
            self.__letters_guessed_list = self.__player_guess.split()
        else:
            indices_of_guess_in_random_word = [index for index, value in enumerate(self.__word) if value == self.__player_guess]
            for index in indices_of_guess_in_random_word:
                self.__letters_guessed_list[index] = self.__player_guess
                    
    def __update_game(self) -> None:
        clear_terminal()
        self.__update_letters_guessed_list()
        self.__update_scoreboard()
        self.__display_high_score()
        self.__display_game_data()

    def reset_word(self) -> str:
        new_word = choice(WORDS_LIST).lower()
        self.__word: str = new_word if(new_word:=choice(WORDS_LIST).lower()) is not self.__word else choice(WORDS_LIST).lower()
        self.__player_guess: str = ""
        self.__letters_guessed_list: list[str] = ["_"] * len(self.__word)
        return self.__word
    
    def reset_player_lives(self) -> None:
        self.__player["lives"] = 6

    def decrement_player_lives(self) -> None:
        self.__player["lives"] -= 1

    def update_user_guess(self, guess:str) -> None:
        self.__player_guess = guess
        self.__update_letters_guessed_list()

    def update_player_points(self) -> None:
        current_points = self.__points + self.__player["lives"]
        self.__points = current_points
        self.__update_scoreboard()

    def get_state(self, key: str = None) -> str | dict | int | list: 
        state = {
            "word": self.__word, 
            "player_guess": self.__player_guess, 
            "letters_guessed": self.__letters_guessed_list, 
            "top":self.__top,
            "player": self.__player,
            "points": self.__points,
            "ranking": self.__get_player_rank()
        }
        if key:
            return state[key]
        return state
    
    def __get_player_rank(self) -> dict[int, list]:
        rankings = [{"name":name, "score":score} for name, score in scoreboard["scores"].items()]
        # Sort key is a function which takes in ranking list, and sorts based on "score" property at each iteration of ranking list
        rankings.sort(key=lambda rankings:rankings["score"], reverse=True)
        return {
            "player_ranking":rankings.index({"name": self.__player["name"], "score": self.__player["score"]}) + 1 or len(scoreboard["scores"]),
            "overall_ranking": rankings
        }

    def play_game(self) -> None:

        self.__update_game()
        print(self.test)
        if str(self.__player_guess).lower() != "quit":

            if not self.__player["lives"]:
                print(DISPLAY_TEXTS["out_of_lives"])
                clear_terminal(2)

            elif self.__player_guess == self.__word or ''.join(self.__letters_guessed_list).lower() == self.__word:
                print(DISPLAY_TEXTS["player_wins"], self.__word)
                clear_terminal(2)
                
                self.update_player_points()
                self.reset_player_lives()
                self.reset_word()
                self.play_game()

            else:
                if not self.__player_guess or self.__player_guess in self.__word:
                    self.__player_guess = input(DISPLAY_TEXTS["user_guess"]).lower()
                    self.play_game()
                else:
                    self.decrement_player_lives()
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
        player_name = input(DISPLAY_TEXTS["get_player_name"]).capitalize()
        clear_terminal()

        print(f"Welcome back, {player_name}") if player_name in scoreboard["scores"] else print(f"Let's play, {player_name}")
        clear_terminal(2)

        print(DISPLAY_TEXTS["ready_to_play"])
        clear_terminal(4.5)

        Hangman(player_name).play_game()

    else:
        print(DISPLAY_TEXTS["quit_game"])
        clear_terminal(2)
