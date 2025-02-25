# 最初に実行するシーン
from Scenes.TitleScene import TitleScene


# デバッグ用 #####################
from Scenes.GameScene import GameScene
from Floor import Floor
from Vector2 import Vector2
start_floor = Floor(Vector2(50, 90), Vector2(70, 90))
next_floor = Floor(Vector2(100, 90), Vector2(120, 90))

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