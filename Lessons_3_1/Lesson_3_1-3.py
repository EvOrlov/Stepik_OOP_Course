class Vector:
    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i,int)])

    def __str__(self):
        if not self.values: return "Пустой вектор"
        else:
            return "Вектор"+f'{tuple(self.values)}'

v1 = Vector(4,1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"