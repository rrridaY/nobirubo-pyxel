class MoveObject:
    """
    移動オブジェクトクラス(始点、終点を持つ)
    シーンのつなぎ目で動かしたいオブジェクトに継承させる
    """
    def move_left(self, speed):
        self.start_pos.x -= speed
        self.end_pos.x -= speed
    def move_right(self, speed):
        self.start_pos.x += speed
        self.end_pos.x += speed
    def fall(self, speed):
        self.start_pos.y += speed
        self.end_pos.y += speed
    