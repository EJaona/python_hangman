import json
from utils.fs import write_to_file, read_from_file, create_file

scoreboard_path = "scoreboard.json"

def create_scoreboard(player_name:str) -> json:
    create_file(scoreboard_path, {"top":{"score":0, "player":None}, "scores":{}})
    add_player_to_scoreboard(player_name)

def add_player_to_scoreboard(player_name:str) -> None:
    scoreboard = read_from_file(scoreboard_path)
    if not player_in_scoreboard(player_name):
        scoreboard["scores"][player_name] = 0
        update_scoreboard_file(scoreboard)

def player_in_scoreboard(player_name:str) -> bool:
    scoreboard = read_from_file(scoreboard_path)
    return player_name in scoreboard["scores"]

def get_player_scoreboard_record(player_name:str) -> int:
    scoreboard = read_from_file(scoreboard_path)
    return scoreboard["scores"][player_name] if player_name in scoreboard["scores"] else 0

def update_scoreboard_file(updated_scoreboard:json) -> None:
    write_to_file(scoreboard_path, updated_scoreboard)

def update_top_record(player_name:str, points:int) -> None:
    scoreboard = read_from_file(scoreboard_path)
    scoreboard["top"] = {"player":player_name, "score": points}
    update_scoreboard_file(scoreboard)

def update_player_scoreboard(player_name:str, points:int) -> int:
    scoreboard = read_from_file(scoreboard_path)
    scoreboard["scores"][player_name] = points
    update_scoreboard_file(scoreboard)
    return scoreboard["scores"][player_name]

def get_top_scoreboard_record() -> dict[str, int]:
    scoreboard = read_from_file(scoreboard_path)
    return {"player":scoreboard["top"]["player"], "score":scoreboard["top"]["score"]}


def get_player_rank(player_name:str) -> int | dict[int, list]:
    scoreboard = read_from_file(scoreboard_path)
    if player_name not in scoreboard["scores"]:
        return len(scoreboard)
    
    ranking_lst = [{"name":name, "score":score} for name, score in scoreboard["scores"].items()]
    # Sort key is a function which takes in ranking list, and sorts based on "score" property at each iteration of ranking list
    ranking_lst.sort(key=lambda ranking_lst:ranking_lst["score"], reverse=True)
    player_rank = ranking_lst.index({"name": player_name, "score": scoreboard["scores"][player_name]})
    return {
        "player":player_rank + 1,
        "overall": ranking_lst
    }
