from pygame_.setup.display_setup  import SCREEN
from pygame_.setup.button_setup import letters as letters_dict
from pygame_.setup.game_setup import pygame
from .pg import create_header_font, create_paragraph_font, clear_screen, delayed_screen_update, was_rect_clicked


def position_x_center(text_width): return (SCREEN.get_width()/2) - (text_width/2)

def display_rect_to_screen(rect, color='black'):
    pygame.draw.rect(SCREEN, color, rect, 2)

def display_image_to_screen(image) -> None: 
    SCREEN.blit(image, (75 , 100))

def display_letters_guessed_to_text(string_list:list[str]) -> None: 
    render_text = create_header_font(' '.join(string_list).capitalize())
    SCREEN.blit(render_text, (position_x_center(render_text.get_width() - 150), 230))

def display_high_score(player:str, score:int) -> None:
    render_player = create_paragraph_font(f"{player or 'TopScore'}")
    render_separator = create_paragraph_font("|")
    render_score = create_paragraph_font(f"{score or 'None'}")
    SCREEN.blits([(render_player, (25, 20)), (render_separator, (render_player.get_width() + 30, 20)), (render_score, (render_player.get_width() + 50, 20))])

def display_player_score(player:str, score:int) -> None:
    render_score = create_paragraph_font(f"{player} : {score}")
    SCREEN.blit(render_score, (775, 20))

def display_player_lives(lives:int) -> None:
    render_lives = create_paragraph_font(f"Lives : {lives}")
    SCREEN.blit(render_lives, (position_x_center(render_lives.get_width()), 20))

def display_text(text:str, position = None) -> None:
    render_text = create_header_font(text)
    centered = (position_x_center(render_text.get_width()), 200)
    SCREEN.blit(render_text, position or centered)

def display_buttons_to_screen() -> None:
    for letter in letters_dict:
        if letters_dict[letter]['is_visible']:
            text = create_paragraph_font(letter)
            rect = SCREEN.blit(text, (letters_dict[letter]['x'] - text.get_width()/2, letters_dict[letter]['y'] - text.get_width()/2))
            letters_dict[letter]["rect"] = rect

def greet_player(player):
    clear_screen()
    if player.is_new_player:
        display_text(f"Let's play, {player.name}!")
    else:
        display_text(f"Welcome back, {player.name}!")
    delayed_screen_update(2000)

def get_letter_clicked() -> str:

        for key in letters_dict:
            mouse_position = pygame.mouse.get_pos()
            letter_obj = letters_dict[key]
            letter_clicked = was_rect_clicked(letter_obj["rect"], mouse_position)

            if letter_clicked and letter_obj["is_visible"]: 
                return key