from helpers.game_props import Game

from helpers.player import Player
from helpers.top_score import TopRecord

class GameState:
    word:str
    lives:int
    player_guess:str 
    letters_guessed:list[str]
    top_record:TopRecord
    player:Player
    points:int
    ranking:dict[int, int]

    def __init__(self, player:Player, top_record:TopRecord, game_props:Game):
        self.word = game_props.word
        self.lives = game_props.lives
        self.points = game_props.points
        self.player_guess = game_props.player_guess
        self.letters_guessed = game_props.letters_guessed_lst
        self.top_record = top_record
        self.player = player
        self.ranking = player.get_scoreboard_ranking()