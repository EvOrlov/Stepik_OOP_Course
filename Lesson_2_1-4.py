import  math


class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, second_point):
        if hasattr(second_point, "x") and hasattr(second_point, "y"):
            return math.hypot((second_point.x - self.x), (second_point.y - self.y))
        else:
            print("Передана не точка")