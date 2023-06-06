from dataclasses import dataclass


@dataclass(kw_only=True)
class Ranking:
    player:int
    overall:int