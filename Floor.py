from Vector2 import Vector2

import pyxel

class Floor:
    """
    床クラス
    usage:
    floor = Floor(Vector2(0, 0), Vector2(0, 0))
    """
    def __init__(self, start_pos:Vector2, end_pos:Vector2):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.length = self.end_pos.x - self.start_pos.x
        self.color = 0

    def draw(self):
        pyxel.line(self.start_pos.x, self.start_pos.y, self.end_pos.x, self.end_pos.y, self.color)