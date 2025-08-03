class Star:
    __slots__ = ("_name", "_massa", "_temp")

    def __init__(self, name, massa, temp):
        self._name = name # имя звезды
        self._massa = massa # масса звезды
        self._temp = temp # температура звезды


class WhiteDwarf(Star):
    """белый карлик"""
    __slots__ = ("_type_star", "_radius")

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star # тип звезды
        self._radius = radius  # радиус звезды в солнечных радиусах

class YellowDwarf(Star):
    """желтый карлик"""
    __slots__ = ("_type_star", "_radius")

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star  # тип звезды
        self._radius = radius  # радиус звезды в солнечных радиусах

class RedGiant(Star):
    """красный гигант"""
    __slots__ = ("_type_star", "_radius")

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star  # тип звезды
        self._radius = radius  # радиус звезды в солнечных радиусах


class Pulsar(Star):
    """пульсар"""
    __slots__ = ("_type_star", "_radius")

    def __init__(self, name, massa, temp, type_star, radius):
        super().__init__(name, massa, temp)
        self._type_star = type_star  # тип звезды
        self._radius = radius  # радиус звезды в солнечных радиусах


stars = [RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
         WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
         WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
         YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)]

white_dwarfs = list(filter(lambda star: isinstance(star, WhiteDwarf), stars))

print(len(white_dwarfs))