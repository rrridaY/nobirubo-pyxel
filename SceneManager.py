# 最初に実行するシーン
from Scenes.TitleScene import TitleScene


# デバッグ用
from Scenes.GameScene import GameScene


class SceneManager:
    # 最初に実行するシーン
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