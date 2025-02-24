import pyxel


# クラスのインポート(シーン)
from Scenes.BaseScene import BaseScene
from Scenes.GameScene import GameScene

# 定数
from constants import *


class TitleScene(BaseScene):
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):  # スペースキーでゲーム開始
            from SceneManager import SceneManager
            SceneManager.change_scene(GameScene())

    def draw(self):
        pyxel.cls(0)
        pyxel.text(SCREEN_WIDTH // 2,SCREEN_HEIGHT // 2, "nobirubo", pyxel.COLOR_WHITE)
