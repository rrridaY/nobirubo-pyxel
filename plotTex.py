from Texture import Texture
from pyxel import blt

# pyxel.blt → plotTexure という関数で呼び出しできるようにする

def plotTexture(x,y,texture:Texture):
    """
    blt関数を使いやすくする関数\n
    クラス引数を用いてblt関数を呼び出す
    """
    #textureの型確認
    if not isinstance(texture, Texture):
        raise TypeError("texture must be Texture type")
    
    #blt関数に引数を渡す
    blt(x, y, texture.imgbnk, texture.origin.x, texture.origin.y, texture.size.x, texture.size.y, texture.colkey)