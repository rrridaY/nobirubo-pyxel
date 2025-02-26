# 最初に実行するシーン
from Scenes.TitleScene import TitleScene


# デバッグ用 #####################
from constants import *
from Scenes.GameScene import GameScene
from Floor import Floor
from Vector2 import Vector2
import random
start_floor = Floor(Vector2(START_PLAYER_POSX-10, 90+1), Vector2(START_PLAYER_POSX+10, 90+1))
a = random.randint(start_floor.end_pos.x + 10, 139)
b = random.randint(a, 140)
next_floor = Floor(Vector2(a, 90+1), Vector2(b, 90+1))

#################################


class SceneManager:
    # 最初に実行するシーン
    current_scene = GameScene(start_floor, next_floor)

    @staticmethod
    def change_scene(scene):
        SceneManager.current_scene = scene

    @staticmethod
    def update():
        SceneManager.current_scene.update()

    @staticmethod
    def draw():
        SceneManager.current_scene.draw()