import pyxel


# クラスのインポート(シーン)
from Scenes.BaseScene import BaseScene
from Scenes.GameScene import GameScene

# クラスのインポート(データ処理)

# 定数
from constants import *


class TitleScene(BaseScene):
    def __init__(self,score=0):
        self.score = score

        self.sharebutton = 0# 予定　新しいボタンクラスをtexture継承で作る
        

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):  # スペースキーでゲーム開始
            from SceneManager import SceneManager
            SceneManager.change_scene(GameScene())

        

    def draw(self):
        pyxel.cls(0)
        pyxel.text(SCREEN_WIDTH // 2,SCREEN_HEIGHT // 2, "nobirubo", pyxel.COLOR_WHITE)
