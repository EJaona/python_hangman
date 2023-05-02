import time
from pygame_hangman.setup.game_setup import pygame
from pygame_hangman.setup.display_setup import SCREEN
import pygame_hangman.helpers.display_helpers  as display_helpers

class Input:

    def __init__(self, position_x, position_y, width, height) -> None:
        self.position_y = position_y
        self.position_x = position_x
        self.user_text:str = ''
        self.collect_input:bool = True
        self.input_box:pygame.Rect = display_helpers.create_rect(position_x, position_y, width, height)
        self.border_color = 'black'
        self.cursor = pygame.Rect(self.input_box.topleft, (5, self.input_box.height))


    def get_text(self, display_text) -> str:

        while self.collect_input:

            display_helpers.clear_screen()
            display_helpers.display_text(display_text, (self.position_x - 150, self.position_y - 100))
            display_helpers.draw_rect_to_screen(self.input_box, self.border_color)
            user_text_rect = SCREEN.blit(display_helpers.create_paragraph_font(self.user_text), (self.position_x, self.position_y))
            
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
        



         