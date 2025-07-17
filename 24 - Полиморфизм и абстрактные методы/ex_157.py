class Track:
    def __init__(self, *args):
        if len(args) == 2 and type(args[0]) != PointTrack and type(args[1]) != PointTrack:

            self.__points = [PointTrack(args[0], args[1])]
        else:
            if all(type(x) == PointTrack for x in args):
                self.__points = list(args)

    @property
    def points(self):
        return tuple((x.x, x.y) for x in self.__points)

    def add_back(self, pt):
        if isinstance(pt, PointTrack):
            self.__points.append(pt)

    def add_front(self, pt):
        if isinstance(pt, PointTrack):
            self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x, y):
        self.x = self.verify_point(x)
        self.y = self.verify_point(y)

    def verify_point(self, point):
        """проверка корректности точки"""
        if type(point) not in (int, float):
            raise TypeError('координаты должны быть числами')
        return point

    def __str__(self):
        return f'PointTrack: {self.x}, {self.y}'




pt = PointTrack(1, 2)
print(pt) # PointTrack: 1, 2

tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)