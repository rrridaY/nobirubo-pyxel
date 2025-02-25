class MoveObject:
    """
    移動オブジェクトクラス
    シーンのつなぎ目で動かしたいオブジェクトに継承させる
    """
    def move_left(self, speed):
        self.start_pos.x -= speed
        self.end_pos.x -= speed
    def move_right(self, speed):
        self.start_pos.x += speed
        self.end_pos.x += speed