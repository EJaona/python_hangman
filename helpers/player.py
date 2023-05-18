from dataclasses import dataclass

@dataclass(kw_only=True)
class Player:
    name:str
    top_score:int
    is_new_player:bool
    
