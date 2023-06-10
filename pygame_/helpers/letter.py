from pygame import Rect

from pygame_.utils.gui import create_paragraph_font


class Letter:
    x:int
    y:int
    rect:Rect
    text:Rect
    is_visible:bool = True

    def __init__(self, *, key:str, x_position:int, y_position:int) -> None:
        self.x = x_position
        self.y = y_position
        self.text = create_paragraph_font(key)

    def update_visibility(self, visibility:bool):
        self.is_visible = visibility

    def set_rect(self, rect:Rect):
        self.rect = rect