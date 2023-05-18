from .display_setup import WIDTH

RADIUS = 30

GAP = 5

start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)

start_y = 350

A = 65

letters = {
    chr(A + i).lower(): {
        "x":start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13)), 
        "y": start_y + ((i // 13) * (GAP + RADIUS * 2)),
        "is_visible": True
    } for i in range(26)
}