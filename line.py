"""使っていません"""

from Vector2 import Vector2
import pyxel

# pyxel.line(self.player_x, START_PLAYER_POSY, self.player_x, START_PLAYER_POSY - self.stick_length, 7)


def line(start_point : Vector2 , end_point : Vector2, color):
    """
    2点間の直線を描画する関数
    """
    pyxel.line(start_point.x, start_point.y, end_point.x, end_point.y, color)
    