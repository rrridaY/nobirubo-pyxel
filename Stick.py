from Vector2 import Vector2
from MoveObject import MoveObject

import pyxel

class Stick(MoveObject):
    """棒クラス"""


    def __init__(self, _start_pos:Vector2, _stick_length:int):
        # 棒の先端の位置
        self.start_pos = _start_pos        
        self.end_pos = Vector2(self.start_pos.x, self.start_pos.y - _stick_length)
        self.length = _stick_length
        self.is_length_decided = False

        # 赤
        self.color = 4

    
    def draw(self):
        if self.length == 0: return
        pyxel.line(self.start_pos.x, self.start_pos.y, self.end_pos.x, self.end_pos.y, self.color)

    def grow(self, STICK_GROWTH_SPEED):
        self.length += STICK_GROWTH_SPEED
        self.end_pos = Vector2(self.start_pos.x, self.start_pos.y - self.length)
    
    def decide_length(self):
        self.is_length_decided = True
        self.end_pos = Vector2(self.start_pos.x + self.length, self.start_pos.y)
    
    # def move_left(self, speed):
    #     self.start_pos.x -= speed
    #     self.end_pos.x -= speed 