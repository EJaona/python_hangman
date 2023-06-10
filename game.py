from main import Hangman
from pygame_.helpers.Input import Input
import pygame_.utils.display as display
from pygame_.setup.display_setup import images
from pygame_.setup.game_setup import pygame, clock
from pygame_.helpers.letter_buttons import LetterButtons
from pygame_.utils.gui import clear_screen, delayed_screen_update

def main(player_name:str) -> None:
    
    # Game state
    game = Hangman(player_name)
    letter_buttons = LetterButtons()
    play = True

    # Greet player
    clear_screen()
    display.text(game.greet_player())
    delayed_screen_update(2000)  

    # Game loop
    while play:
        word = game.get_state().word
        image_to_display = images[game.get_state().lives]
        
        clock.tick(60)
        clear_screen()

        display.image_to_screen(image_to_display)
        display.word_indicator(game.get_state().letters_guessed)
        display.player_lives(game.get_state().lives)

        display.high_score_data(
            game.get_state().top_record.player,
            game.get_state().top_record.score
        )

        display.player_score_data(
            game.get_state().player.name,
            game.get_state().points
        )

        letter_buttons.display_to_screen()

        if not game.get_state().lives:
            delayed_screen_update(500)

            display.text(f"GAME OVER, MAN!")
            delayed_screen_update(2000)

            display.text(f"The word was '{word.capitalize()}'")
            delayed_screen_update(2000)

            play = False

        
        # Should be is_guess_correct
        if "".join(game.get_state().letters_guessed) == word:

            delayed_screen_update(1000)

            display.text(f"{word.capitalize()}")
            delayed_screen_update(1500)

            display.text(f"+ {game.get_state().lives}")
            delayed_screen_update(2000)
            
            letter_buttons.reset_display()

            # Update state
            game.update_player_points()
            game.reset_game()

        # Event loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                play = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                letter_clicked = letter_buttons.get_letter_clicked()

                if letter_clicked in word:
                    game.update_user_guess(letter_clicked)
                else:
                    game.decrement_lives()
                    
                letter_buttons.remove_from_screen(letter_clicked)

            if event.type == pygame.KEYDOWN:
                
                letter_pressed = letter_buttons.get_letter_pressed(event.key)

                if letter_pressed in letter_buttons._letters_dict:

                    if letter_pressed in word:
                        game.update_user_guess(letter_pressed)
                    else:
                        game.decrement_lives()

                    letter_buttons.remove_from_screen(letter_pressed)

        pygame.display.flip()

if __name__ == "__main__":
    
    input_box = Input(x=300, y=200, width=400, height=50)
    player_name = input_box.get_text("Whats your name, player?")
    main(player_name)
    pygame.quit()