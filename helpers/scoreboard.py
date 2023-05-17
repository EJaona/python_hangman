from os import path
from ..utils.fs import write_to_file, read_from_file

def create_scoreboard(file_path:str = "../score_board.json") -> dict:
    if not path.exists(file_path): write_to_file(file_path, {"top":{"score":0, "player":""}})
    return read_from_file(file_path)