from Vector2 import Vector2
from MoveObject import MoveObject

import pyxel

from constants import STICK_MAX_LENGTH, STICK_GROWTH_SPEED,STICK_DEFAULT_LENGTH

class Stick(MoveObject):
    """棒クラス"""


    def __init__(self, _start_pos:Vector2, _stick_length:int):
        # 棒の先端の位置
        self.start_pos = _start_pos        
        self.end_pos = Vector2(self.start_pos.x, self.start_pos.y - _stick_length)
        self.length = _stick_length
        self.is_length_decided = False
        
        # 倒れるときの座標リスト
        self.fall_pos : list[Vector2] = []

        # 棒の色
        self.color = 4

    def update(self):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) :
            # 棒の長さが最大長さに達していない場合
            if self.length < STICK_MAX_LENGTH:
                self.grow(STICK_GROWTH_SPEED)

            # 棒の長さが最大長さに達した場合
            else:
                self.decide_length()
                from Scenes.GameScene import GameStatusManager, GameStatus
                GameStatusManager.change_status(GameStatus.CALC_STICK_SPIN_AMIM)
                
        

            # 左クリックが解除されたら
        elif pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            self.decide_length()
            from Scenes.GameScene import GameStatusManager, GameStatus
            GameStatusManager.change_status(GameStatus.CALC_STICK_SPIN_AMIM)

    
    def draw(self):
        if self.length == 0: return
        pyxel.line(self.start_pos.x, self.start_pos.y, self.end_pos.x, self.end_pos.y, self.color)

    def grow(self, STICK_GROWTH_SPEED):
        self.length += STICK_GROWTH_SPEED
        self.end_pos = Vector2(self.start_pos.x, self.start_pos.y - self.length)
    
    def decide_length(self):
        self.is_length_decided = True
        # self.end_pos = Vector2(self.start_pos.x + self.length, self.start_pos.y)

    def change_color(self, color):
        self.color = color

    def create_spin_pos_with_digree(self,total_degree:int,flame_length:int = None):
        """フレーム数に応じてスティックを落下させる座標をリストで返す"""

        # 座標リスト
        edge_trajectory:list[Vector2] = []

        
        if flame_length:
            for i in range(flame_length):
                # 回転中の座標を追加
                edge_trajectory.append(spin(self.start_pos, self.end_pos, total_degree/flame_length*i))
        
        
        # 最終的な座標を追加
        edge_trajectory.append(spin(self.start_pos, self.end_pos, total_degree))

        return edge_trajectory
    
    # def move_left(self, speed):
    #     self.start_pos.x -= speed
    #     self.end_pos.x -= speed 

def create_start_stick(player_pos:Vector2):
    return Stick(Vector2(player_pos.x,player_pos.y - 1), STICK_DEFAULT_LENGTH)


def spin(org:Vector2, edge:Vector2, degree):
    """Vector2クラスを使って回転させる関数
    
    org: 原点
    edge: 回転軸
    degree: 角度
    """
    # 回転軸のベクトル
    edge_vector = edge - org
    # 回転軸のベクトルの長さ
    edge_length = edge_vector.length()
    # 回転軸のベクトルの角度
    edge_degree = edge_vector.angle()
    # 回転軸のベクトルの角度を変更(回転角はy軸下向き正の時計回りなので加算でよい)
    edge_degree += degree
    # 回転後の座標
    edge = Vector2(edge_length, 0).rotate(edge_degree) + org

    # 座標を四捨五入
    edge.x = round(edge.x)
    edge.y = round(edge.y)
    return Vector2(edge.x, edge.y)