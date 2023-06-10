from helpers.ranking import Ranking
from utils.scoreboard import get_ranking, get_player_record, update_player_record

class Player:

    def __init__(self, player_name):
        self.name:str = player_name
        self.top_score:int = get_player_record(player_name)
        self.is_new_player:bool = not self.top_score

    def update_scoreboard(self, score:int):
       self.top_score = update_player_record(self.name, score)

    def get_scoreboard_ranking(self):
        return Ranking(**get_ranking(self.name))
    
    def greet(self) -> str:
        
        if self.is_new_player:
            return f"Let's play, {self.name}!"
        else:
            return f"Welcome back, {self.name}!"
        