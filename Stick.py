from Vector2 import Vector2

import pyxel

class Stick:
    """棒クラス"""


    def __init__(self, start_pos:Vector2, stick_length:int):
        # 棒の先端の位置
        self.start_pos = start_pos        
        self.end_pos = Vector2(self.start_pos.x, self.start_pos.y - stick_length)
        self.length = stick_length
        self.is_length_decided = False

    
    def draw(self):
        pyxel.line(self.start_pos.x, self.start_pos.y, self.end_pos.x, self.end_pos.y, 7)

    def grow(self, STICK_GROWTH_SPEED):
        self.length += STICK_GROWTH_SPEED
        self.end_pos = Vector2(self.start_pos.x, self.start_pos.y - self.length)
    
    def decide_length(self):
        self.is_length_decided = True
        self.end_pos = Vector2(self.start_pos.x + self.length, self.start_pos.y)
