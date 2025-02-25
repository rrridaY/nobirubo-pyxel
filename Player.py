from Vector2 import Vector2
from MoveObject import MoveObject
from Texture import Texture


import pyxel

class Player(MoveObject):
    """
    プレイヤークラス
    """
    def __init__(self, _pos:Vector2,_texture: Texture = None):
        self.pos = _pos
        self.texture = _texture
        self.is_crossed = False
        self.color = 7
        self.size = 10


    def update(self):
        pass

    def draw(self):
        if self.texture != None:
            Texture.draw(self.pos.x, self.pos.y)
        else:
            pyxel.rect(self.pos.x - self.size, self.pos.y - self.size, self.size , self.size, self.color)
    
    
    def move_left(self, speed):
        self.pos.x -= speed
    def move_right(self, speed):
        self.pos.x += speed
    def fall(self, speed):
        self.pos.y += speed