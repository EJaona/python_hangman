import math

from hang_man_class import Hangman
from pygame_hangman.helpers.Input import Input
from pygame_hangman.setup.game_setup import pygame, clock
import pygame_hangman.setup.display_setup as display_setup
import pygame_hangman.setup.button_setup as letter_buttons 
import pygame_hangman.helpers.display_helpers as display_helpers

def main(player_name:str) -> None:
    
# Game state
    hangman = Hangman(player_name)
    hangman.update_player_lives(6)
    word = hangman.get_state("word")
    image_to_display = (len(display_setup.images) - 1) - hangman.get_state("player")["lives"]
    play = True

    # Greet player
    display_helpers.greet_player(hangman.get_state('player'))

    # Game loop
    while play:

        clock.tick(60)
        display_helpers.clear_screen()

        display_helpers.draw_image_to_screen(image_to_display)
        display_helpers.display_letters_guessed_to_text(hangman.get_state("guesses"))
        display_helpers.display_player_lives(hangman.get_state("player")["lives"])

        display_helpers.display_high_score(
            hangman.get_state("high_score")["player"],
            hangman.get_state("high_score")["score"]
        )

        display_helpers.display_player_score(
            hangman.get_state("player")["name"],
            hangman.get_state("points")
        )

        display_helpers.draw_buttons_to_screen()

        if not hangman.get_state("player")["lives"]:
            display_helpers.delayed_screen_update(500)

            display_helpers.display_text(f"GAME OVER, MAN!")
            display_helpers.delayed_screen_update(2000)

            display_helpers.display_text(f"The word was '{word.capitalize()}'")
            display_helpers.delayed_screen_update(2000)

            play = False

        if "".join(hangman.get_state("guesses")) == word:

            display_helpers.delayed_screen_update(1000)

            display_helpers.display_text(f"{word.capitalize()}")
            display_helpers.delayed_screen_update(1500)

            display_helpers.display_text(f"+ {hangman.get_state('player')['lives']}")
            display_helpers.delayed_screen_update(2000)
            
            for letter in letter_buttons.letters: letter["is_visible"] = True

            # Update state
            current_points = hangman.get_state("points") + hangman.get_state("player")["lives"]
            hangman.update_player_points(current_points)
            hangman.update_player_lives(6)
            word = hangman.reset_word()
            image_to_display = (len(display_setup.images) - 1) - hangman.get_state("player")["lives"]

        else:
            
            for event in pygame.event.get():

                match event.type:
                    case pygame.QUIT:
                        play = False
                    case pygame.MOUSEBUTTONDOWN:
                        position_x, position_y = pygame.mouse.get_pos()

                        for letter in letter_buttons.letters:
                            x, y, character, = letter["x"], letter["y"], letter["letter"]
                            event_distance_from_letter = math.sqrt((x - position_x)**2 + (y - position_y)**2)

                            if letter["is_visible"] and event_distance_from_letter <= letter_buttons.RADIUS :

                                if character in word:
                                    hangman.update_user_guess(character)

                                else:
                                    image_to_display += 1
                                    hangman.update_player_lives(hangman.get_state("player")["lives"] - 1)

                                letter["is_visible"] = False

                    case pygame.KEYDOWN:
                        key_pressed = pygame.key.name(event.key)

                        for letter in letter_buttons.letters:
                            character, is_visible = letter["letter"], letter["is_visible"]

                            if key_pressed == character and is_visible:

                                if key_pressed in word:
                                    hangman.update_user_guess(key_pressed)

                                else:
                                    image_to_display += 1
                                    hangman.update_player_lives(hangman.get_state("player")["lives"] - 1)

                                letter["is_visible"] = False

        pygame.display.flip()

if __name__ == "__main__":
    
    player_name = Input(300, 200, 400, 50).get_text("Whats your name, player?")
    main(player_name)
pygame.quit()