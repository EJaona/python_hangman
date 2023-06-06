from main import Hangman
from pygame_.helpers.Input import Input
import pygame_.utils.display as display
from pygame_.setup.display_setup import images
from pygame_.setup.game_setup import pygame, clock
from pygame_.setup.button_setup import letters as letter_dict
from pygame_.utils.pg import clear_screen, delayed_screen_update

def main(player_name:str) -> None:
    
    # Game state
    game = Hangman(player_name)
    play = True

    # Greet player
    display.greet_player(game.get_state().player)
            
    # Game loop
    while play:
        word = game.get_state().word
        image_to_display = images[game.get_state().lives]
        
        clock.tick(60)
        clear_screen()

        display.display_image_to_screen(image_to_display)
        display.display_letters_guessed_to_text(game.get_state().letters_guessed)
        display.display_player_lives(game.get_state().lives)

        display.display_high_score(
            game.get_state().top_record.player,
            game.get_state().top_record.score
        )

        display.display_player_score(
            game.get_state().player.name,
            game.get_state().points
        )

        display.display_buttons_to_screen()

        if not game.get_state().lives:
            delayed_screen_update(500)

            display.display_text(f"GAME OVER, MAN!")
            delayed_screen_update(2000)

            display.display_text(f"The word was '{word.capitalize()}'")
            delayed_screen_update(2000)

            play = False

        if "".join(game.get_state().letters_guessed) == word:

            delayed_screen_update(1000)

            display.display_text(f"{word.capitalize()}")
            delayed_screen_update(1500)

            display.display_text(f"+ {game.get_state().lives}")
            delayed_screen_update(2000)
            
            for letter_key in letter_dict: letter_dict[letter_key]["is_visible"] = True

            # Update state
            game.update_player_points()
            game.reset_game()

        # Event loop
        for event in pygame.event.get():

            match event.type:
                
                case pygame.QUIT:
                    play = False

                case pygame.MOUSEBUTTONDOWN:
                    letter_clicked = display.get_letter_clicked()

                    if letter_clicked:

                        if letter_clicked in word:      
                            game.update_user_guess(letter_clicked)
                            letter_dict[letter_clicked]["is_visible"] = False
                        else:
                            game.decrement_lives()
                            letter_dict[letter_clicked]["is_visible"] = False

                            
                case pygame.KEYDOWN:
                    letter_pressed = pygame.key.name(event.key)
                    letter_obj = letter_dict[letter_pressed] if letter_pressed in letter_dict else {"is_visible":False}
    
                    if letter_obj["is_visible"]:

                        if letter_pressed in word:
                            game.update_user_guess(letter_pressed)
                        else:
                            game.decrement_lives()

                    letter_obj["is_visible"] = False

        pygame.display.flip()

if __name__ == "__main__":
    
    player_name = Input(x=300, y=200, width=400, height=50).get_text("Whats your name, player?")
    main(player_name)
    pygame.quit()