import time

from pygame_package.setup.game_setup import pygame
from pygame_package.setup.display_setup import SCREEN
from .pg import create_rect, create_paragraph_font, clear_screen
from .display  import display_text, display_rect_to_screen

class Input:

    def __init__(self, *, x, y, width, height, color="black") -> None:
        self.y:int = y
        self.x:int = x
        self.user_text:str = ''
        self.collect_input:bool = True
        self.input_box:pygame.Rect = create_rect(x, y, width, height)
        self.border_color:str = color
        self.cursor = pygame.Rect(self.input_box.topleft, (5, self.input_box.height))


    def get_text(self, text) -> str:

        while self.collect_input:

            clear_screen()
            display_text(text, (self.x - 150, self.y - 100))
            display_rect_to_screen(self.input_box, self.border_color)
            user_text_rect = SCREEN.blit(create_paragraph_font(self.user_text), (self.x, self.y))
            
            for event in pygame.event.get():

                match event.type:
                    case pygame.QUIT:
                        pygame.quit()

                    case pygame.KEYDOWN:

                        if event.key == pygame.K_BACKSPACE:
                   
                            if len(self.user_text):
                                self.user_text = self.user_text[:-1]
                                self.cursor.topleft = (user_text_rect.right - 20, user_text_rect.top)

                            else:
                                self.cursor.topleft = self.input_box.topleft

                        elif event.key == pygame.K_RETURN:
                            self.collect_input = False

                        else:
                            self.user_text += event.unicode
                            self.cursor.topleft = (user_text_rect.right + 20, user_text_rect.top)

            if time.time() % 1 > 0.5:
                pygame.draw.rect(SCREEN, 'black', self.cursor)

            pygame.display.flip()

        return self.user_text
        



         