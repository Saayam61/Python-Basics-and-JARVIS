# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def makeVector(self):
        print(f'The vector is {self.x}i + {self.y}j')
    
class Vector3D(Vector2D):
    def __init__(self, x, y, z) -> None:
        super().__init__(x, y)
        self.z = z
    
    def makeVector(self):
        print(f'The vector is {self.x}i + {self.y}j + {self.z}k')
    
v1 = Vector2D(1, 2)
v2 = Vector3D(1, 2, 3)
v1.makeVector()
v2.makeVector()
        