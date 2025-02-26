
# ライブラリのインポート

import pyxel

# 関数のインポート

from plotTex import plotTexture
from line import line

# クラスのインポート(データ処理)
import random
from Texture import Texture # イメージバンクの画像情報を保持するクラス
from Vector2 import Vector2
from Player import Player
from Floor import Floor
from Stick import Stick

# クラスのインポート(シーン)
from Scenes.BaseScene import BaseScene

# 定数
from constants import *




class GameScene(BaseScene):
    def __init__(
            self,
            current_floor : Floor,
            next_floor : Floor,
            prev_stick : Stick = Stick(Vector2(0, 90), 0),
            score: int = 0
            ):
        # プレイヤーの初期位置
        # self.player_pos = Vector2(START_PLAYER_POSX, START_PLAYER_POSY)
        self.player = Player(Vector2(START_PLAYER_POSX, START_PLAYER_POSY))
        
        
        
        # 棒
        self.stick = Stick(Vector2(START_PLAYER_POSX, START_PLAYER_POSY), STICK_DEFAULT_LENGTH)

        # ひとつ前の棒
        self.prev_stick = prev_stick



        # 現在の床
        self.current_floor = current_floor
        # 次の床    
        self.next_floor = next_floor

        # スコア
        self.score = score

        # GAME OVER描画用
        self.game_over_flame = 0



    def update(self):
        if pyxel.btnp(pyxel.KEY_R):
            from SceneManager import SceneManager
            SceneManager.change_scene(GameScene())

        # デバッグ用 30フレームごとにプリント ####
        if pyxel.frame_count % 30 == 0:
            print("player: ", self.player.pos.x,"next_floor_start: ", self.next_floor.start_pos.x, "next_floor_end: ", self.next_floor.end_pos.x)

        #######################################

        # 棒が伸びる前の処理
        if not self.stick.is_length_decided : 
        
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) :
                # 棒の長さが最大長さに達していない場合
                if self.stick.length < STICK_MAX_LENGTH:
                    self.stick.grow(STICK_GROWTH_SPEED)

                # 棒の長さが最大長さに達した場合
                else:
                    self.stick.decide_length()
            

            # 左クリックが解除されたら
            elif pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                self.stick.decide_length()
        
        # 棒が伸びた後の処理
        elif self.stick.is_length_decided :
            # プレイヤーが移動中
            if not self.player.is_crossed:
                self.player.move_right(PLAYER_MOVE_SPEED)
                if self.player.is_x_reached(self.stick.end_pos.x+self.player.size.x):
                    self.player.is_crossed = True

            
            # プレイヤーが移動完了後
            elif self.player.is_crossed:
                if self.player.is_on_floor(self.next_floor):

                    # プレイヤーが床に乗る
                    start_floor = Floor(Vector2(START_PLAYER_POSX-10, 90+1), Vector2(START_PLAYER_POSX+10, 90+1))
                    a = random.randint(start_floor.end_pos.x + 10, 139)
                    b = random.randint(a, 140)
                    next_floor = Floor(Vector2(a, 90+1), Vector2(b, 90+1))
                    from SceneManager import SceneManager
                    SceneManager.change_scene(GameScene(start_floor, next_floor, score=self.score+1))


                else:
                    # プレイヤーが床から落ちる
                    self.player.fall(PLAYER_FALL_SPEED)
                    if self.player.pos.y > SCREEN_HEIGHT:
                        self.game_over_flame += 1
                        if self.game_over_flame > 30 * 3:
                            # ゲーム終了
                            pyxel.quit()


        # デバッグ　左に動かす #################
        if pyxel.btn(pyxel.KEY_LEFT):
        #     self.stick.move_left(1)
        #     self.current_floor.move_left(1)
        #     self.next_floor.move_left(1)
        #     self.prev_stick.move_left(1)
            self.player.move_left(1)
        # デバッグ　右に動かす
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.move_right(1)


        #######################################

    def draw(self):
        pyxel.cls(1)
        # 棒を描画
        self.stick.draw()
        self.prev_stick.draw()


        # 床を描画
        self.current_floor.draw()
        self.next_floor.draw()

        # プレイヤーを描画
        # pyxel.rect(self.player.pos.x-10, self.player.pos.y-10, 10, 10, 7)
        self.player.draw()


        # スコアを描画
        pyxel.text(80, 20, "SCORE: " + str(self.score), 7)

        # playerの座標を描画（点）
        pyxel.pset(self.player.pos.x, self.player.pos.y, 6)

        # GAME OVERを描画
        if self.game_over_flame > 0:
            pyxel.text(60, 60, "GAME OVER", 8)
