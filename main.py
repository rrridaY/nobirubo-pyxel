# ライブラリのインポート

import pyxel

# 関数のインポート

from plotTex import plotTexture

# クラスのインポート

from Texture import Texture # イメージバンクの画像情報を保持するクラス
from Vector2 import Vector2

# 定数(スクリーン)
SCREEN_WIDTH = 160  
SCREEN_HEIGHT = 120

# 定数(プレイヤー)
START_PLAYER_POSX = 40
START_PLAYER_POSY = 90

# 定数(棒)
STICK_WIDTH = 2
STICK_DEFAULT_LENGTH = 10    # 棒の初期長さ
STICK_GROWTH_SPEED = 1       # 棒の伸びる早さ
STICK_MAX_LENGTH = 100       # 棒の伸び上限



# シーン
TITLE_SCENE = "title"
PLAY_SCENE = "play"





class BaseScene:
    def update(self):
        pass
    
    def draw(self):
        pass

class TitleScene(BaseScene):
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):  # スペースキーでゲーム開始
            SceneManager.change_scene(GameScene())

    def draw(self):
        pyxel.cls(0)
        pyxel.text(SCREEN_WIDTH // 2,SCREEN_HEIGHT // 2, "nobirubo", pyxel.COLOR_WHITE)

class GameScene(BaseScene):
    def __init__(self):
        # プレイヤーの初期位置
        self.player_x = START_PLAYER_POSX
        # 棒の長さ
        self.stick_length = STICK_DEFAULT_LENGTH


    def update(self):
        if pyxel.btnp(pyxel.KEY_R):  # スペースキーでゲーム開始
            SceneManager.change_scene(GameScene())
        # 左クリックで棒を伸ばす (長さ上限有り)
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.stick_length < STICK_MAX_LENGTH:
            self.stick_length += STICK_GROWTH_SPEED



    def draw(self):
        pyxel.cls(1)
        # プレイヤー位置から棒を描画
        pyxel.line(self.player_x, START_PLAYER_POSY, self.player_x, START_PLAYER_POSY - self.stick_length, 7)


class SceneManager:
    current_scene = GameScene()

    @staticmethod
    def change_scene(scene):
        SceneManager.current_scene = scene

    @staticmethod
    def update():
        SceneManager.current_scene.update()

    @staticmethod
    def draw():
        SceneManager.current_scene.draw()

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT, title="koha game")
        pyxel.run(SceneManager.update, SceneManager.draw)




App()