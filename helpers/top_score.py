from utils.scoreboard import get_top_scoreboard_record, update_top_record

class TopRecord:
    player:str
    score:int

    def __init__(self) -> None:
        self.player = get_top_scoreboard_record()["player"]
        self.score = get_top_scoreboard_record()["score"]

    def update(self, player_name, score) -> None:
        update_top_record(player_name, score)
        self.player = get_top_scoreboard_record()["player"]
        self.score = get_top_scoreboard_record()["score"]