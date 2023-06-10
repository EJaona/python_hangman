import json
from utils.fs import write_to_file, read_from_file, create_file

scoreboard_path = "scoreboard.json"

def create_scoreboard(player_name:str) -> json:
    create_file(scoreboard_path, {"top":{"score":0, "player":None}, "scores":{}})
    add_player(player_name)

def update_scoreboard(updated_scoreboard:json) -> None:
    write_to_file(scoreboard_path, updated_scoreboard)

def add_player(player_name:str) -> None:
    scoreboard = read_from_file(scoreboard_path)
    if not get_player_record(player_name):
        scoreboard["scores"][player_name] = 0
        update_scoreboard(scoreboard)

def get_player_record(player_name:str) -> int|bool:
    scoreboard = read_from_file(scoreboard_path)
    return scoreboard["scores"][player_name] if player_name in scoreboard["scores"] else False

def update_player_record(player_name:str, points:int) -> int:
    scoreboard = read_from_file(scoreboard_path)
    scoreboard["scores"][player_name] = points
    update_scoreboard(scoreboard)
    return scoreboard["scores"][player_name]

def get_top_record() -> dict[str, int]:
    scoreboard = read_from_file(scoreboard_path)
    return {"player":scoreboard["top"]["player"], "score":scoreboard["top"]["score"]}

def update_top_record(player_name:str, points:int) -> None:
    scoreboard = read_from_file(scoreboard_path)
    scoreboard["top"] = {"player":player_name, "score": points}
    update_scoreboard(scoreboard)

def get_ranking(player_name:str) -> int | dict[int, list]:
    scoreboard = read_from_file(scoreboard_path)
    if player_name not in scoreboard["scores"]:
        return len(scoreboard)
    
    player_list = [{"name":name, "score":score} for name, score in scoreboard["scores"].items()]
    player_list.sort(key=lambda ranking_lst:ranking_lst["score"], reverse=True)
    player_rank = player_list.index({"name": player_name, "score": scoreboard["scores"][player_name]})
    return {
        "player":player_rank + 1,
        "player_list": player_list
    }
