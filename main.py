# ライブラリのインポート
import pyxel


# クラスのインポート(シーン)
from SceneManager import SceneManager


# 定数
from constants import *


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT, title="koha game")
        pyxel.load("my_resource.pyxres")       
        pyxel.run(SceneManager.update, SceneManager.draw)




App()