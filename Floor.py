from Vector2 import Vector2
from MoveObject import MoveObject


import pyxel
import random

from constants import  GROUND_HEIGHT, FLOOR_X_MAX, START_PLAYER_POSX , NEXT_FLOOR_MIN_DISTANCE

class Floor(MoveObject):
    """
    床クラス
    usage:
    floor = Floor(Vector2(0, 0), Vector2(0, 0))
    """
    def __init__(self, start_pos:Vector2, end_pos:Vector2):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.length = self.end_pos.x - self.start_pos.x
        self.color = 3

    def draw(self):
        pyxel.line(self.start_pos.x, self.start_pos.y, self.end_pos.x, self.end_pos.y, self.color)

    def create_next_floor(self,floor_length:int = None):
        """既存の床インスタンスを基に次の床を生成する
        
        Args:
            floor_length (int, optional): 床の長さ上限を指定できる 
            
        """
        # 床の始点X座標
        next_floor_start_x = random.randint(self.end_pos.x + NEXT_FLOOR_MIN_DISTANCE, FLOOR_X_MAX)
        
        # 床の終点X座標
        if floor_length: # 床の長さ上限を設定する場合
            next_floor_end_x = random.randint(next_floor_start_x, next_floor_start_x + floor_length)
        
        else:            # 床の長さ上限を設定しない場合
            next_floor_end_x = random.randint(next_floor_start_x, FLOOR_X_MAX)
        
        print(f"next_floor_start_x:{next_floor_start_x}, next_floor_end_x:{next_floor_end_x}")
        return Floor(Vector2(next_floor_start_x, GROUND_HEIGHT), Vector2(next_floor_end_x, GROUND_HEIGHT))
        
    


def create_start_floor(
        start_pos : Vector2 = Vector2(START_PLAYER_POSX - 10, GROUND_HEIGHT),
        end_pos : Vector2 = Vector2(START_PLAYER_POSX + 10, GROUND_HEIGHT)
        ):
    if not isinstance(start_pos, Vector2) or not isinstance(end_pos, Vector2):
        raise TypeError("start_pos and end_pos must be Vector2")
    return Floor(Vector2(start_pos.x, start_pos.y), Vector2(end_pos.x, end_pos.y))