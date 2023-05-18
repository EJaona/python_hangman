from random import choice

from helpers.top_score import Top
from helpers.player import Player
from utils.constants import WORDS_LIST, SHOULD_PLAY_RESPONSES, DISPLAY_TEXTS
from utils.fs import clear_terminal, colorGreen, colorYellow, underline
from utils.scoreboard \
    import create_scoreboard, get_player_rank, get_player_scoreboard_record,\
          get_top_scoreboard_record, player_in_scoreboard, update_player_scoreboard, update_top_scoreboard


class Hangman:

    def __init__(self, player_name:str) -> None:
        create_scoreboard()
        player_name = player_name.capitalize()

        self._top: Top = get_top_scoreboard_record()
        self._word: str = choice(WORDS_LIST).lower()
        self._points: int = 0
        self._lives = 6

        self._player_guess: str = None
        self._letters_guessed_lst: list[str] = ["_"] * len(self._word)
        self._player: Player = Player(
            name = player_name,
            top_score = get_player_scoreboard_record(player_name),
            is_new_player = not player_in_scoreboard(player_name)
        )


    def __display_high_score(self) -> None: 
        print(f"{underline(self._top.player or 'Top_Score')}: {colorYellow(self._top.score or 'None')} | {underline(self._player.name)}: {colorYellow(self._points)}\n")
    
    def __display_game_data(self) -> None: 
        print(f"Points: {colorGreen(self._points)} Word: {colorGreen(' '.join(self._letters_guessed_lst).capitalize())} Lives: {colorGreen(self._lives)}\n")

    def __update_scoreboard(self) -> None:
        if self._player.is_new_player or self._points > self._player.top_score:
            updated_scoreboard_player_score = update_player_scoreboard(self._player.name, self._points)
            self._player.top_score = updated_scoreboard_player_score

        if self._points > self._top.score:
            updated_scoreboard_top_score = update_top_scoreboard(self._player.name, self._points)
            self._top = updated_scoreboard_top_score

    def __update_letters_guessed_list(self):
        if self._player_guess == self._word:
            self._letters_guessed_lst = self._player_guess.split()
        else:
            indices_of_guess_in_random_word = [index for index, value in enumerate(self._word) if value == self._player_guess]
            for index in indices_of_guess_in_random_word:
                self._letters_guessed_lst[index] = self._player_guess
                    
    def __update_game(self) -> None:
        clear_terminal()
        self.__update_letters_guessed_list()
        self.__update_scoreboard()
        self.__display_high_score()
        self.__display_game_data()

    def reset_word(self) -> str:
        new_word = choice(WORDS_LIST).lower()
        self._word: str = new_word if(new_word:=choice(WORDS_LIST).lower()) is not self._word else choice(WORDS_LIST).lower()
        self._player_guess: str = ""
        self._letters_guessed_lst: list[str] = ["_"] * len(self._word)
        return self._word
    
    def reset_lives(self) -> None:
        self._lives = 6

    def decrement_lives(self) -> None:
        self._lives -= 1

    def update_user_guess(self, guess:str) -> None:
        self._player_guess = guess
        self.__update_letters_guessed_list()

    def update_player_points(self) -> None:
        current_points = self._points + self._lives
        self._points = current_points
        self.__update_scoreboard()

    def get_state(self, key: str = None) -> str | Top | int | list | Player: 
        state = {
            "word": self._word,
            "lives": self._lives,
            "player_guess": self._player_guess, 
            "letters_guessed": self._letters_guessed_lst, 
            "top":self._top,
            "player": self._player,
            "points": self._points,
            "ranking": get_player_rank(self._player.name)
        }
        return state[key] if key else state

    def play_game(self) -> None:
        
        self.__update_game()

        if str(self._player_guess).lower() == "quit":
            print(DISPLAY_TEXTS["quit_game"])
            return clear_terminal(2)
        
        if not self._lives:
            print(DISPLAY_TEXTS["out_of_lives"])
            return clear_terminal(2)

        if str(self._player_guess).lower() == "rank":
            ranking = get_player_rank(self._player.name)
            print(DISPLAY_TEXTS['player_ranking'], f"{ranking['player']} out of {len(ranking['overall'])}")
            clear_terminal(2)
        
        if self._player_guess == self._word or ''.join(self._letters_guessed_lst).lower() == self._word:
            print(DISPLAY_TEXTS["player_wins"], self._word)
            clear_terminal(2)
            
            self.update_player_points()
            self.reset_lives()
            self.reset_word()
            return self.play_game()

        elif not self._player_guess or self._player_guess in self._word:
                self._player_guess = input(DISPLAY_TEXTS["user_guess"]).lower()
                return self.play_game()
        else:
            self.decrement_lives()
            self._player_guess = None
            clear_terminal()
            return self.play_game()

            

            
if __name__ == "__main__":

    clear_terminal()

    if input(DISPLAY_TEXTS["should_play_game"]).capitalize() in SHOULD_PLAY_RESPONSES:
        clear_terminal()
        player_name = input(DISPLAY_TEXTS["get_player_name"]).capitalize()
        game = Hangman(player_name)
        clear_terminal()

        print(f"Welcome back, {player_name}") if player_in_scoreboard(player_name) else print(f"Let's play, {player_name}")
        clear_terminal(2)

        print(DISPLAY_TEXTS["ready_to_play"])
        clear_terminal(4.5)

        game.play_game()

    else:
        print(DISPLAY_TEXTS["quit_game"])
        clear_terminal(2)
