from helpers.game_props import Game
from helpers.game_state import GameState
from helpers.top_score import TopRecord
from helpers.player import Player
from utils.constants import SHOULD_PLAY_RESPONSES, DISPLAY_TEXTS
from utils.io import clear_terminal, colorGreen, colorYellow, underline
from utils.scoreboard import create_scoreboard


class Hangman:
    _game_props = Game()
    _top_record:TopRecord
    _player:Player
    
    def __init__(self, player_name:str) -> None:
        player_name = player_name.capitalize()
        create_scoreboard(player_name)
        self._top_record = TopRecord()
        self._player = Player(player_name)

    def __display_high_score(self) -> None:
        top_player:str = underline(self._top_record.player or 'Top_Score')
        top_score:str = colorYellow(self._top_record.score or 'None')
        player_name:str = underline(self._player.name)
        player_score:str = colorYellow(self._player.top_score)

        if top_player == player_name:
            print(f"{top_player}: {top_score}\n")
        else:
            print(f"{top_player}: {top_score} | {player_name}: {player_score}\n")
    
    def __display_game_props(self) -> None:
        points = f"Points: {colorGreen(self._game_props.points)}"
        word_hint = f"Word: {colorGreen(self._game_props.format_letters_guessed(' ').capitalize())}"
        lives = f"Lives: {colorGreen(self._game_props.lives)}"
        print(f"{points} {word_hint} {lives}\n")

    def __update_scoreboard(self) -> None:
        if self._game_props.points > self._player.top_score:
            self._player.update_scoreboard(self._game_props.points)

        if self._game_props.points > self._top_record.score:
            self._top_record.update(self._player.name, self._game_props.points)
                    
    def __update_game(self) -> None:
        clear_terminal()
        self.__update_scoreboard()
        self.__display_high_score()
        self.__display_game_props()

    def greet_player(self) -> str:
        return self._player.greet()
    
    def reset_game(self) -> str:
        self._game_props.reset()

    def decrement_lives(self) -> None:
        self._game_props.decrement_lives()

    def update_user_guess(self, guess:str) -> None:
        self._game_props.set_guess(guess)

    def update_player_points(self) -> None:
        self._game_props.update_points()
        self.__update_scoreboard()

    def get_state(self) -> GameState: 
        return GameState(player=self._player, top_record=self._top_record, game_props=self._game_props)
    
    def play(self) -> None:
        
        self.__update_game()

        if self._game_props.player_guess == "quit":
            print(DISPLAY_TEXTS["quit_game"])
            return clear_terminal(2)
        
        if not self._game_props.lives:
            print(DISPLAY_TEXTS["out_of_lives"])
            return clear_terminal(2)

        if self._game_props.player_guess == "rank":
            ranking = self._player.get_scoreboard_ranking()
            print(DISPLAY_TEXTS['player_ranking'], f"{ranking.player} out of {len(ranking.player_list)}")
            clear_terminal(2)
        
        if self._game_props.word_guessed():
            print(DISPLAY_TEXTS["player_wins"], self._game_props.word)
            clear_terminal(2)
            
            self.update_player_points()
            self._game_props.reset()
            return self.play()

        if not self._game_props.player_guess or self._game_props.guess_in_word():
                player_input = input(DISPLAY_TEXTS["user_guess"])
                self._game_props.set_guess(player_input)
                return self.play()
        else:
            self.decrement_lives()
            self._game_props.set_guess()
            clear_terminal()
            return self.play()

            

if __name__ == "__main__":

    clear_terminal()

    if input(DISPLAY_TEXTS["should_play_game"]).capitalize() in SHOULD_PLAY_RESPONSES:
        clear_terminal()

        name = input(DISPLAY_TEXTS["get_player_name"])
        game = Hangman(name)
        clear_terminal()

        print(game.greet_player())
        clear_terminal(2)

        print(DISPLAY_TEXTS["ready_to_play"])
        clear_terminal(4.5)

        game.play()

    else:
        print(DISPLAY_TEXTS["quit_game"])
        clear_terminal(2)
