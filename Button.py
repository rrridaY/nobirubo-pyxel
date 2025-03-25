# クラスのインポート
from Vector2 import Vector2
from Texture import Texture

# モジュールのインポート
import pyxel
import webbrowser # web　SNSシェア用

# 定数のインポート
from constants import GAME_URL




class Button(Texture):
    """
    ボタンクラス
    """
    def __init__(self, pos:Vector2,texture:Texture,event_func=None):
        self.pos = pos # ボタンを配置する座標
        self.texture = texture # ボタンのテクスチャ
        super().__init__(texture.imgbnk, texture.origin, texture.size)
        self.click_event_func = event_func

    def update(self):
        pass

    def draw(self):
        self.texture.draw(self.pos.x, self.pos.y)

    def is_clicked(self,click_pos:Vector2):
        return self.pos.x <= click_pos.x <= self.pos.x + self.texture.size.x and self.pos.y <= click_pos.y <= self.pos.y + self.texture.size.y
    
    def click_event(self, **kwargs):
        if self.click_event_func:
            self.click_event_func(self, **kwargs)
        else:
            print("click event is None")

        


class URLButton(Button):
    def __init__(self, pos:Vector2, texture:Texture, url = None):
        super().__init__(pos, texture)
        self.url = url

    def open_url(self): # リンク付きボタンのクリック時の処理
        if self.url:
            print(f"open url {self.url}")
            webbrowser.open(self.url)

        elif self.url is None:
            print("instance url is None")
    


class TwitterShareButton(Button):
    def __init__(self, pos:Vector2, texture:Texture):
        super().__init__(pos, texture)

    @staticmethod
    def open_shareURL_with_score(self,score): # リンク付きボタンのクリック時の処理
        print(f"open_shareURL_with_score: {score}") 
        payload = "https://twitter.com/intent/tweet?text=pyxel-nobirubo-%E3%81%A7%E3%82%B9%E3%82%B3%E3%82%A2%20{}%20%E7%82%B9%E3%82%92%E7%8D%B2%E5%BE%97%E3%81%97%E3%81%BE%E3%81%97%E3%81%9F%EF%BC%81%0A&url={}"          
        share_url = payload.format(score, GAME_URL)
        webbrowser.open(share_url)