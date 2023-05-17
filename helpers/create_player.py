from utils.fs import read_from_file


scoreboard = read_from_file('score_board.json')

def create_player(name:str) -> dict[str, int, int, bool]:
    name = name.capitalize()
    return{
        "name": name,
        "score": scoreboard["scores"][name] if name in scoreboard["scores"] else 0,
        "lives": 6,
        "is_new_player": name not in scoreboard["scores"]
    }
