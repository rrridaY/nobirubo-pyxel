import pyxel

class BaseScene:
    def __init__(self):
        self.fade_alpha = 255  # 透明度（フェードイン・アウト用）

    def fade_in(self):
        if self.fade_alpha > 0:
            self.fade_alpha -= 5

    def fade_out(self):
        if self.fade_alpha < 255:
            self.fade_alpha += 5

    def update(self):
        self.fade_in()  # どのシーンでもフェードインが適用される

    def draw(self):
        pass
