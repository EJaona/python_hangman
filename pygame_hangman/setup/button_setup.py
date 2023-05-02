from pygame_hangman.setup.display_setup import WIDTH

RADIUS = 30

GAP = 5

startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)

starty = 350

A = 65

letters = [
    {
        "x":startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13)), 
        "y": starty + ((i // 13) * (GAP + RADIUS * 2)),
        "letter": str(chr(A + i)).lower(),
        "is_visible": True
    } 
    for i in range(26)
]