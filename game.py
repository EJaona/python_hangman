from main import Hangman
from helpers import display, pg, Input
from pygame_package.setup.game_setup import pygame, clock
from pygame_package.setup.display_setup import images
from pygame_package.setup.button_setup import letters as letter_dict

def main(player_name:str) -> None:
    
    # Game state
    game = Hangman(player_name)
    word = game.get_state("word")
    play = True

    # Greet player
    pg.greet_player(game.get_state('player'))

    # Game loop
    while play:

        image_to_display = images[game.get_state("player")["lives"]]
        
        clock.tick(60)
        pg.clear_screen()

        display.display_image_to_screen(image_to_display)
        display.display_letters_guessed_to_text(game.get_state("letters_guessed"))
        display.display_player_lives(game.get_state("player")["lives"])

        display.display_high_score(
            game.get_state("top")["player"],
            game.get_state("top")["score"]
        )

        display.display_player_score(
            game.get_state("player")["name"],
            game.get_state("points")
        )

        # display.display_buttons_to_screen()
        display.display_buttons_to_screen()

        if not game.get_state("player")["lives"]:
            pg.delayed_screen_update(500)

            display.display_text(f"GAME OVER, MAN!")
            pg.delayed_screen_update(2000)

            display.display_text(f"The word was '{word.capitalize()}'")
            pg.delayed_screen_update(2000)

            play = False

        if "".join(game.get_state("letters_guessed")) == word:

            pg.delayed_screen_update(1000)

            display.display_text(f"{word.capitalize()}")
            pg.delayed_screen_update(1500)

            display.display_text(f"+ {game.get_state('player')['lives']}")
            pg.delayed_screen_update(2000)
            
            for letter_key in letter_dict: letter_dict[letter_key]["is_visible"] = True

            # Update state
            game.update_player_points()
            game.reset_player_lives()
            word = game.reset_word()

        else:
            
            for event in pygame.event.get():

                match event.type:
                    case pygame.QUIT:
                        play = False

                    case pygame.MOUSEBUTTONDOWN:

                        for letter in letter_dict:
                            
                            mouse_position = pygame.mouse.get_pos()
                            letter_obj = letter_dict[letter]
                            letter_clicked = pg.was_rect_clicked(letter_obj["rect"], mouse_position)
                            is_visible = letter_obj["is_visible"]

                            if letter_clicked and is_visible:

                                if letter in word:      
                                    game.update_user_guess(letter)
                                else:
                                    game.decrement_player_lives()

                                letter_obj["is_visible"] = False
                                
                    case pygame.KEYDOWN:
                        letter_pressed = pygame.key.name(event.key)
                        letter_obj = letter_dict[letter_pressed]
      
                        if letter_obj["is_visible"]:

                            if letter_pressed in word:
                                game.update_user_guess(letter_pressed)
                            else:
                                game.decrement_player_lives()

                        letter_obj["is_visible"] = False

        pygame.display.flip()

if __name__ == "__main__":
    
    player_name = Input.Input(x=300, y=200, width=400, height=50).get_text("Whats your name, player?")
    main(player_name)
    pygame.quit()