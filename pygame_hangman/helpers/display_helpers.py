from pygame_hangman.setup.display_setup  import SCREEN, game_font, letter_font, images
from pygame_hangman.setup.button_setup import letters
from pygame_hangman.setup.game_setup import pygame

def clear_screen(): 
    SCREEN.fill('white')

def position_x_center(text_width): return (SCREEN.get_width()/2) - (text_width/2)

def create_header_font(text:str, color:str = 'black') -> str: 
    return game_font.render(text, 1, color)
    
def create_paragraph_font(text:str, color:str = 'black') -> pygame.Rect: 
    return letter_font.render(text, 1, color)

def create_rect(position_x, position_y, width, height) -> pygame.Rect:
    return pygame.Rect((position_x, position_y), (width, height))

def draw_rect_to_screen(rect, color='black'):
    pygame.draw.rect(SCREEN, color, rect, 2)

def draw_image_to_screen(img_number:int) -> None: 
    SCREEN.blit(images[img_number], (75 , 100))

def delayed_screen_update(time:int) -> None:
    pygame.display.update()
    pygame.time.wait(time)
    clear_screen()

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

def draw_buttons_to_screen() -> None:
    for letter in letters:
        if letter['is_visible']:
            text = create_paragraph_font(letter['letter'])
            SCREEN.blit(text, (letter['x'] - text.get_width()/2, letter['y'] - text.get_width()/2))

def greet_player(player):
    clear_screen()
    if player['is_new_player']:
        display_text(f"Let's play, {player['name']}!")
    else:
        display_text(f"Welcome back, {player['name']}!")
    delayed_screen_update(2000)