
# ライブラリのインポート

import pyxel

# 関数のインポート

from plotTex import plotTexture
from line import line

# クラスのインポート(データ処理)

from Texture import Texture # イメージバンクの画像情報を保持するクラス
from Vector2 import Vector2
from Floor import Floor
from Stick import Stick

# クラスのインポート(シーン)
from Scenes.BaseScene import BaseScene

# 定数
from constants import *




class GameScene(BaseScene):
    def __init__(self,current_floor : Floor,next_floor : Floor):
        # プレイヤーの初期位置
        self.player_pos = Vector2(START_PLAYER_POSX, START_PLAYER_POSY)
        
        
        
        # 棒　after refactoring
        self.stick = Stick(self.player_pos, STICK_DEFAULT_LENGTH)



        # 現在の床
        self.current_floor = current_floor
        # 次の床    
        self.next_floor = next_floor



    def update(self):
        if pyxel.btnp(pyxel.KEY_R):
            from SceneManager import SceneManager
            SceneManager.change_scene(GameScene())

        if self.stick.is_length_decided : pass
        
        elif pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) :
            # 棒の長さが最大長さに達していない場合
            if self.stick.length < STICK_MAX_LENGTH:
                self.stick.grow(STICK_GROWTH_SPEED)

            # 棒の長さが最大長さに達した場合
            else:
                self.stick.decide_length()
        

        # 左クリックが解除されたら
        elif pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            self.stick.decide_length()


    def draw(self):
        pyxel.cls(1)
        # 棒を描画
        self.stick.draw()


        # 床を描画
        self.current_floor.draw()
        self.next_floor.draw()