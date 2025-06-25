class ItemAttrs:
    _fields = ['x', 'y']

    def __getitem__(self, key):
        return getattr(self, self._fields[key])

    def __setitem__(self, key, value):
        setattr(self, self._fields[key], value)

class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Point(1, 2.5)
x = pt[0]   # 1
print(x)
y = pt[1]   # 2.5
print(y)
pt[0] = 10
print(pt.x)  # 10