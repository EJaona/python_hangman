import json
from os import system
from time import sleep

def read_from_file(path):
    with open(path, 'r') as file:
       return json.load( file )

def write_to_file(path:str, data:any):
    with open(path, 'w') as file:
        file.write( json.dumps( data , indent=4 ))

def underline (value:str | int):
    return f"\x1b[4m{value}\x1b[0m"

def colorYellow (value:str | int):
    return f"\x1b[33m{value}\x1b[0m"

def colorGreen (value:str | int):
    return f"\x1b[32m{value}\x1b[0m"

def clear_terminal(time:int=0):
    sleep(time)
    system('clear')