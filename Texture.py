from Vector2 import Vector2

import pyxel



class Origin(Vector2):
    """imgsrcの左上の座標"""
    def __init__(self, x, y):
        super().__init__(x, y)

class Size(Vector2):
    """imgsrcの大きさ"""
    def __init__(self, width, height):
        super().__init__(width, height)

class Texture(Origin, Size):
    """
    イメージバンク画像を管理できるクラス\n
    Texture(<画像バンク番号>,<画像の左上の座標>,<画像の大きさ>,[colkey])\n
    img: 画像バンクの番号\n
    usage:
    imgtarget = Texture(img, Origin(0, 0), Size(16, 16))
    """
    def __init__(self, img, origin, size, colkey=None):
        self.origin = origin
        self.size = size
        self.imgbnk = img
        self.colkey = colkey
    
    def draw(self, x, y):
        """
        画像を描画する関数
        """
        pyxel.blt(x, y, self.imgbnk, self.origin.x, self.origin.y, self.size.x, self.size.y, self.colkey)