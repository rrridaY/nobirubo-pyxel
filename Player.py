from Vector2 import Vector2
from MoveObject import MoveObject
from Texture import Texture
from Floor import Floor


import pyxel

from constants import PLAYER_MOVE_SPEED

class Player(MoveObject):
    """
    プレイヤークラス
    """
    def __init__(self, _pos:Vector2,_texture: Texture = None):
        self.pos = _pos
        self.texture = _texture
        self.is_crossed = False
        self.color = 7
        if self.texture != None:
            self.size = Vector2(self.texture.size.x, self.texture.size.y)
        else:
            self.size = Vector2(5, 10)


    def update(self,stick_end_pos:Vector2):
        # プレイヤーが移動中
        self.move_right(PLAYER_MOVE_SPEED)
        if self.is_x_reached(stick_end_pos.x + self.size.x):
            from Scenes.GameScene import GameStatusManager, GameStatus
            GameStatusManager.change_status(GameStatus.PLAYER_REACHED_STICK_END)
        

    def draw(self):
        if self.texture == None:
            pyxel.rect(self.pos.x - self.size.x, self.pos.y - self.size.y, self.size.x , self.size.y, self.color)
        elif self.texture != None:
            Texture.draw(self.pos.x, self.pos.y)

    def is_x_reached(self, x):
        return self.pos.x > x
    
    
    
    def is_x_in_range(self, start, end):
        return start <= self.pos.x <= end
    
    def is_on_floor(self, floor : Floor):
        return floor.start_pos.x <= self.pos.x <= floor.end_pos.x + self.size.x
    
    
    def move_left(self, speed):
        self.pos.x -= speed
    def move_right(self, speed):
        self.pos.x += speed
    def fall(self, speed):
        self.pos.y += speed