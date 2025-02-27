from Vector2 import Vector2
from MoveObject import MoveObject

import pyxel

from constants import STICK_MAX_LENGTH, STICK_GROWTH_SPEED

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

    def update(self):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) :
            # 棒の長さが最大長さに達していない場合
            if self.length < STICK_MAX_LENGTH:
                self.grow(STICK_GROWTH_SPEED)

            # 棒の長さが最大長さに達した場合
            else:
                self.decide_length()
                from Scenes.GameScene import GameStatusManager, GameStatus
                GameStatusManager.change_status(GameStatus.PLAYER_MOVING)
                
        

            # 左クリックが解除されたら
        elif pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            self.decide_length()
            from Scenes.GameScene import GameStatusManager, GameStatus
            GameStatusManager.change_status(GameStatus.PLAYER_MOVING)

    
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