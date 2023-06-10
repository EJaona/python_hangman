from time import sleep
from os import system


def underline (value:str | int) -> str: 
    return f"\x1b[4m{value}\x1b[0m"

def colorYellow (value:str | int) -> str: 
    return f"\x1b[33m{value}\x1b[0m"

def colorGreen (value:str | int) -> str: 
    return f"\x1b[32m{value}\x1b[0m"

def clear_terminal(time:int = 0) -> None:
    sleep(time)
    system('clear')