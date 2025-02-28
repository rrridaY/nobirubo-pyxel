from Vector2 import Vector2
from Texture import Texture

import pyxel


class Button(Texture):
    """
    ボタンクラス
    """
    def __init__(self, pos:Vector2,texture:Texture):
        self.pos = pos
        self.texture = texture
        super().__init__(texture.imgbnk, texture.origin, texture.size)
        self.is_pressed = False

    def update(self):
        pass

    def draw(self):
        self.texture.draw(self.pos.x, self.pos.y)

    def is_pressed(self,click_pos:Vector2):
        return self.pos.x <= click_pos.x <= self.pos.x + self.texture.size.x and self.pos.y <= click_pos.y <= self.pos.y + self.texture.size.y
    