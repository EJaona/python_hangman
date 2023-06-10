import pygame
from pygame_.helpers.letter import Letter
from pygame_.utils.gui import was_rect_clicked
from ..setup.display_setup import SCREEN, WIDTH as screen_width

class LetterButtons:
    
    _radius:int = 30
    _gap:int = 5
    _start_x:int
    _start_y:int = 350
    _ascii_start_at:int = 65
    _letters_dict:dict[str, Letter]

    def __init__(self) -> None:
        self._start_x = round((screen_width - (self._radius * 2 + self._gap) * 13) / 2)
        self._letters_dict = {
            chr(self._ascii_start_at + i).lower(): Letter(
                key = chr(self._ascii_start_at + i).lower(),
                x_position = self._start_x + self._gap * 2 + ((self._radius * 2 + self._gap) * (i % 13)),
                y_position = self._start_y + ((i // 13) * (self._gap + self._radius * 2))
            ) for i in range(26)
        }

    def reset_display(self):
        for letter in self._letters_dict:
            self._letters_dict[letter].update_visibility(True)

    def display_to_screen(self) -> None:
        for letter in self._letters_dict:
            if self._letters_dict[letter].is_visible:
                text = self._letters_dict[letter].text
                rect = SCREEN.blit(text, (self._letters_dict[letter].x - text.get_width()/2, self._letters_dict[letter].y - text.get_width()/2))
                self._letters_dict[letter].set_rect(rect)

    def remove_from_screen(self, letter) -> None:
        if letter in self._letters_dict:
            self._letters_dict[letter].update_visibility(False)

    def get_letter_clicked(self) -> str:

        for key in self._letters_dict:
            mouse_position = pygame.mouse.get_pos()
            letter_obj = self._letters_dict[key]
            letter_clicked = was_rect_clicked(letter_obj.rect, mouse_position)

            if letter_clicked and letter_obj.is_visible: 
                return key
            
    def get_letter_pressed(self, key):
        letter_pressed = pygame.key.name(key)
        if letter_pressed in self._letters_dict and self._letters_dict[letter_pressed].is_visible:
            return letter_pressed 
        
