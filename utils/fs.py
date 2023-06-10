import json
from os import path

def read_from_file(path:str) -> json:
    with open(path, 'r') as file:
       return json.load( file )
    
def write_to_file(path:str, data:dict) -> None:
    with open(path, 'w') as file:
        file.write( json.dumps( data , indent=4 ))

def create_file(file_path:str, file_value) -> json:
    if not path.exists(file_path): write_to_file(file_path, file_value)
    return read_from_file(file_path)

