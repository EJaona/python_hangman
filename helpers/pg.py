from pygame_package.setup.display_setup  import SCREEN, game_font, letter_font
from pygame_package.setup.game_setup import pygame
from . import display

def create_header_font(text:str, color:str = 'black') -> str: 
    return game_font.render(text, 1, color)
    
def create_paragraph_font(text:str, color:str = 'black') -> pygame.Rect: 
    return letter_font.render(text, 1, color)

def create_rect(position_x, position_y, width, height) -> pygame.Rect:
    return pygame.Rect((position_x, position_y), (width, height))

def was_rect_clicked(rect, mouse_position):
    return rect.collidepoint(mouse_position)

def clear_screen(): 
    SCREEN.fill('white')

def position_x_center(text_width): return (SCREEN.get_width()/2) - (text_width/2)

def delayed_screen_update(time:int = 0) -> None:
    pygame.display.update()
    pygame.time.wait(time)
    clear_screen()

def greet_player(player):
    clear_screen()
    if player['is_new_player']:
        display.display_text(f"Let's play, {player['name']}!")
    else:
        display.display_text(f"Welcome back, {player['name']}!")
    delayed_screen_update(2000)