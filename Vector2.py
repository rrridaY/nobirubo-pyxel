import math # 3/2 追加


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        usage:
        a = Vector2(1, 2)
        b = Vector2(3, 4)
        c = a + b
        """
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        usage:
        a = Vector2(1, 2)
        b = Vector2(3, 4)
        c = a - b
        """
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def __str__(self):
        return f"({self.x}, {self.y})"
    

    # ここから回転関連の関数 3/2追加
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def angle(self):
        return math.degrees(math.atan2(self.y, self.x))
    
    def rotate(self, angle):
        rad = math.radians(angle)
        x = self.x * math.cos(rad) - self.y * math.sin(rad)
        y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector2(x, y)
    
    def moveto(self,other):
        self.x = other.x
        self.y = other.y
        return Vector2(self.x,self.y)
    ############################