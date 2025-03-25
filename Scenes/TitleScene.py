import pyxel


# クラスのインポート(シーン)
from Scenes.BaseScene import BaseScene
from Scenes.GameScene import GameScene

# クラスのインポート(データ処理)
from Floor import Floor
from Vector2 import Vector2
from Button import Button
from Texture import Texture

# 関数のインポート
from Floor import create_start_floor

# 定数
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


start_floor:Floor = create_start_floor()
next_floor = start_floor.create_next_floor()

Xbutton = Button(pos=Vector2(20, 80), texture=Texture(0, Vector2(0, 24), Vector2(16, 17),colkey=pyxel.COLOR_BLACK), url="https://twitter.com")



class TitleScene(BaseScene):
    def __init__(self,score=0):
        super().__init__() # baseSceneのinitを呼び出す
        self.score = score

        self.sharebutton = Xbutton# 予定　新しいボタンクラスをtexture継承で作る


        

    def update(self):
        super().update()
        if pyxel.btnp(pyxel.KEY_SPACE):  # スペースキーでゲーム開始
            from SceneManager import SceneManager
            SceneManager.change_scene(GameScene(start_floor, next_floor))
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            # マウスのクリック位置を取得
            clicked_pos = Vector2(pyxel.mouse_x, pyxel.mouse_y)

            # シェア用ボタンがクリックされた場合
            if self.sharebutton.is_clicked(clicked_pos):
                print("Share button is clicked")
                self.sharebutton.open_url(self.score)
        

    def draw(self):
        pyxel.mouse(True)
        pyxel.cls(1)
        pyxel.text(60,20, "nobirubo", pyxel.COLOR_WHITE)
        self.sharebutton.draw()
        pyxel.text(self.sharebutton.pos.x + self.sharebutton.texture.size.x, 
                   self.sharebutton.pos.y + 5, 
                   f"<-Share\nYour Score: {self.score}",
                   pyxel.COLOR_WHITE
                   )
