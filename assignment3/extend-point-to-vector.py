############### Task 5 ###############

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
            return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
         if not isinstance(other, Point):
              return False
         return self.x == other.x and self.y == other.y

    def distance(self, other):
         x_diff = (self.x - other.x) ** 2
         y_diff = (self.y - other.y) ** 2
         return math.sqrt(x_diff + y_diff)
         

class Vector(Point):

    def __str__(self):
        return f"Vector{self.x},{self.y}"

    def __add__(self, other):
         updated_x = self.x + other.x
         updated_y = self.y + other.y
         return Vector(updated_x, updated_y)

# --- Debugging ---
print("---Running test---")
p1 = Point(1, 2)
p2 = Point(4, 6)
p3 = Point(1, 2)

print(f"\nPoint 1: {p1}")
print(f"\nPoint 1: {p2}")
print(f"\nIs Point 1 equal to Point 3? {p1 == p3}")
print(f"\nDistance between p1 and p2: {p1.distance(p2)}")

print("\n --- Vector test ---")
v1 = Vector(2, 3)
v2 = Vector(4, 1)

print(f"\nVector 1: {v1}")
print(f"\nVector 2: {v2}")
v3 = v1 + v2
print(f"\nSum of Vectors: \nVector 1 + Vector 2 = {v3}")