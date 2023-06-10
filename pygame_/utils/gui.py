from pygame_.setup.display_setup  import SCREEN, game_font, letter_font
from pygame_.setup.game_setup import pygame

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
