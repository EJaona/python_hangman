from dataclasses import dataclass

@dataclass(kw_only=True)
class Top:
    player:str
    score:int