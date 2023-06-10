from pygame_.setup.display_setup  import SCREEN
from pygame_.setup.game_setup import pygame
from .gui import create_header_font, create_paragraph_font


def position_x_center(text_width): return (SCREEN.get_width()/2) - (text_width/2)

def display_rect_to_screen(rect, color='black'):
    pygame.draw.rect(SCREEN, color, rect, 2)

def image_to_screen(image) -> None: 
    SCREEN.blit(image, (75 , 100))

def word_indicator(string_list:list[str]) -> None: 
    render_text = create_header_font(' '.join(string_list).capitalize())
    SCREEN.blit(render_text, (position_x_center(render_text.get_width() - 150), 230))

def high_score_data(player:str, score:int) -> None:
    render_player = create_paragraph_font(f"{player or 'TopScore'}")
    render_separator = create_paragraph_font("|")
    render_score = create_paragraph_font(f"{score or 'None'}")
    SCREEN.blits([(render_player, (25, 20)), (render_separator, (render_player.get_width() + 30, 20)), (render_score, (render_player.get_width() + 50, 20))])

def player_score_data(player:str, score:int) -> None:
    render_score = create_paragraph_font(f"{player} : {score}")
    SCREEN.blit(render_score, (775, 20))

def player_lives(lives:int) -> None:
    render_lives = create_paragraph_font(f"Lives : {lives}")
    SCREEN.blit(render_lives, (position_x_center(render_lives.get_width()), 20))

def text(text:str, position = None) -> None:
    render_text = create_header_font(text)
    centered = (position_x_center(render_text.get_width()), 200)
    SCREEN.blit(render_text, position or centered)
