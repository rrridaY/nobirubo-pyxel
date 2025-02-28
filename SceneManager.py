# 最初に実行するシーン
from Scenes.TitleScene import TitleScene


# デバッグ用 #####################
from constants import *
from Scenes.GameScene import GameScene
from Floor import Floor
from Floor import create_start_floor
start_floor:Floor = create_start_floor()
next_floor = start_floor.create_next_floor()
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