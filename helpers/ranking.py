from dataclasses import dataclass


@dataclass(kw_only=True)
class Ranking:
    player:int
    player_list:list