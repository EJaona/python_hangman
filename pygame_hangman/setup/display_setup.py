import os
from pygame_hangman.setup.game_setup import pygame

WIDTH, HEIGHT = 1000, 500

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

images = [pygame.image.load(f'./images/hangman{index}.png') for index, value in enumerate((os.listdir('./images')))]

game_font = pygame.font.SysFont('comicsans', 60)

letter_font = pygame.font.SysFont('comicsans', 40)