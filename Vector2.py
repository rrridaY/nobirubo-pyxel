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