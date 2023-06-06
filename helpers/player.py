from helpers.ranking import Ranking
from utils.scoreboard import get_player_rank, get_player_scoreboard_record, player_in_scoreboard, update_player_scoreboard

class Player:
    name:str
    top_score:int
    is_new_player:bool

    def __init__(self, player_name):
        self.name = player_name
        self.top_score = get_player_scoreboard_record(player_name)
        self.is_new_player = not player_in_scoreboard(player_name)

    def update_scoreboard(self, score:int):
       self.top_score = update_player_scoreboard(self.name, score)

    def get_scoreboard_ranking(self):
        return Ranking(**get_player_rank(self.name))