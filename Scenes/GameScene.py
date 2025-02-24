
# ライブラリのインポート

import pyxel

# 関数のインポート

from plotTex import plotTexture
from line import line

# クラスのインポート(データ処理)

from Texture import Texture # イメージバンクの画像情報を保持するクラス
from Vector2 import Vector2

# クラスのインポート(シーン)
from Scenes.BaseScene import BaseScene

# 定数
from constants import *




class GameScene(BaseScene):
    def __init__(self):
        # プレイヤーの初期位置
        self.player_pos = Vector2(START_PLAYER_POSX, START_PLAYER_POSY)
        # 棒の長さ
        self.stick_length = STICK_DEFAULT_LENGTH
        # 棒の長さが確定した状態かどうか
        self.is_stick_length_decided = False
        # 棒の先端の位置
        self.stick_end_pos = Vector2(self.player_pos.x, self.player_pos.y - self.stick_length)


    def update(self):
        if pyxel.btnp(pyxel.KEY_R):
            from SceneManager import SceneManager
            SceneManager.change_scene(GameScene())

        if self.is_stick_length_decided: pass
        
        elif pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) :
            # 棒の長さが最大長さに達していない場合
            if self.stick_length < STICK_MAX_LENGTH:
                self.stick_length += STICK_GROWTH_SPEED
                self.stick_end_pos = Vector2(self.player_pos.x, self.player_pos.y - self.stick_length)
            # 棒の長さが最大長さに達した場合
            else:
                self.is_stick_length_decided = True
                self.stick_end_pos = Vector2(self.player_pos.x + self.stick_length, self.player_pos.y)
        

        # 左クリックが解除されたら
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            self.is_stick_length_decided = True
            self.stick_end_pos = Vector2(self.player_pos.x + self.stick_length, self.player_pos.y)



    def draw(self):
        pyxel.cls(1)
        # プレイヤー位置から棒を描画
        if not self.is_stick_length_decided:
            stick_color = 7
            pyxel.text(SCREEN_WIDTH -40,SCREEN_HEIGHT // 5, f"{self.stick_length}nobase!", pyxel.COLOR_WHITE)
        else:
            stick_color = 8
            pyxel.text(SCREEN_WIDTH -40,SCREEN_HEIGHT // 5, f"{self.stick_length}decided!", pyxel.COLOR_WHITE)

        line(self.player_pos, self.stick_end_pos, stick_color)