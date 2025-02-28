
# ライブラリのインポート

import pyxel
import webbrowser # web　SNSシェア用
import random
import enum

# 関数のインポート

from plotTex import plotTexture
from line import line
from Stick import create_start_stick

# クラスのインポート(データ処理)

from Texture import Texture # イメージバンクの画像情報を保持するクラス
from Vector2 import Vector2
from Player import Player
from Floor import Floor
from Stick import Stick

# クラスのインポート(シーン)
from Scenes.BaseScene import BaseScene

# 定数
from constants import *


# GameScene状態管理用クラス
class GameStatus(enum.Enum):
    
    INPUT_STICK_LENGTH = enum.auto()
    """棒の長さを受け付け中"""

    PLAYER_MOVING = enum.auto()
    """棒の長さを決定後、プレイヤーが移動中"""

    PLAYER_REACHED_STICK_END = enum.auto()
    """プレイヤーが棒に到達したとき"""

    PLAYER_ON_NEXT_FLOOR = enum.auto()
    """プレイヤーが床に乗ったとき"""

    PLAYER_NOT_ON_NEXT_FLOOR = enum.auto()
    """プレイヤーが床に乗らなかったとき"""

    PLAYER_RETURNED_TO_START_POS = enum.auto()
    """プレイヤーが戻ったとき"""

    GAMEOVER = enum.auto()
    """ゲームオーバー"""

# GameScene状態管理用クラス
class GameStatusManager:
    current_status = GameStatus.INPUT_STICK_LENGTH

    @staticmethod
    def change_status(status):
        GameStatusManager.current_status = status
    
    def is_status(status):
        return GameStatusManager.current_status == status


# GameSceneで全オブジェクトを左に移動
def move_all_left(objs, speed):
    for obj in objs:
        obj.move_left(speed)


class GameScene(BaseScene):
    def __init__(
            self,
            current_floor : Floor,
            next_floor : Floor,
            prev_stick : Stick = Stick(Vector2(0, 90), 0),
            game_status : GameStatus = GameStatus.INPUT_STICK_LENGTH,
            score: int = 0
            ):
        # プレイヤーの初期位置
        self.player = Player(Vector2(START_PLAYER_POSX, current_floor.start_pos.y))
        
        # 棒
        self.stick = create_start_stick(self.player.pos)

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

        # シーンの状態を初期化
        # game_status = GameStatus.INPUT_STICK_LENGTH
        GameStatusManager.change_status(game_status)



    def update(self):
        # デバッグ用 シーンリセット #############
        if pyxel.btnp(pyxel.KEY_R):
            start_floor = self.current_floor
            next_floor = start_floor.create_next_floor()
            from SceneManager import SceneManager
            SceneManager.change_scene(GameScene(start_floor, next_floor))


        #######################################


        # デバッグ用 30フレームごとにプリント ####
        # if pyxel.frame_count % 30 == 0:
        #     print("player: ", self.player.pos.x,"next_floor_start: ", self.next_floor.start_pos.x, "next_floor_end: ", self.next_floor.end_pos.x)

        #######################################

        # 棒が伸びる前の処理
        if GameStatusManager.is_status(GameStatus.INPUT_STICK_LENGTH):
        # if GameStatusManager.current_status == GameStatus.INPUT_STICK_LENGTH :
            self.stick.update()

        # 棒が伸びた後の処理
        elif GameStatusManager.is_status(GameStatus.PLAYER_MOVING):
        # elif GameStatusManager.current_status == GameStatus.PLAYER_MOVING:
            self.player.update(self.stick)

        # プレイヤーが棒に到達した後の処理
        elif GameStatusManager.is_status(GameStatus.PLAYER_REACHED_STICK_END):
            if self.player.is_on_floor(self.next_floor):
                GameStatusManager.change_status(GameStatus.PLAYER_ON_NEXT_FLOOR)
            elif self.player.is_on_floor(self.current_floor):
                self.stick = create_start_stick(self.player.pos)
                GameStatusManager.change_status(GameStatus.INPUT_STICK_LENGTH)
            else:
                GameStatusManager.change_status(GameStatus.PLAYER_NOT_ON_NEXT_FLOOR)

        # プレイヤーが床に乗った後の処理
        elif GameStatusManager.is_status(GameStatus.PLAYER_ON_NEXT_FLOOR):
            move_all_left([self.stick, self.current_floor, self.next_floor, self.prev_stick,self.player], ALL_OBJECTS_MOVE_SPEED)
            if self.player.pos.x < START_PLAYER_POSX:
                GameStatusManager.change_status(GameStatus.PLAYER_RETURNED_TO_START_POS)


        elif GameStatusManager.is_status(GameStatus.PLAYER_NOT_ON_NEXT_FLOOR):
            # プレイヤーが床から落ちる
            self.player.fall(PLAYER_FALL_SPEED)
            if self.player.pos.y > SCREEN_HEIGHT:
                self.game_over_flame += 1
                if self.game_over_flame > 30 * 2:
                    # ゲーム終了
                    pyxel.quit()

        # プレイヤーがスタート地点に戻った後の処理
        elif GameStatusManager.is_status(GameStatus.PLAYER_RETURNED_TO_START_POS):
            start_floor = self.next_floor
            next_floor = start_floor.create_next_floor()
            from SceneManager import SceneManager
            SceneManager.change_scene(GameScene(start_floor, next_floor, prev_stick=self.stick, score=self.score+1))

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
        # 背景を描画
        pyxel.cls(1)
        # マウスを描画
        pyxel.mouse(True)

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

        # デバッグ用 playerの座標を描画（点）
        # pyxel.pset(self.player.pos.x, self.player.pos.y, 6)

        # GAME OVERを描画
        if self.game_over_flame > 0:
            pyxel.text(60, 60, "GAME OVER", 8)
