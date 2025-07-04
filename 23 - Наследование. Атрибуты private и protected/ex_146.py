class Furniture:
    """мебель для дома"""
    def __init__(self, name, weight):
        self._name = Furniture.__verify_name(name) # название мебели
        self._weight = Furniture.__verify_weight(weight) # вес мебели

    def __verify_name(text):
        """для проверки корректности имени"""
        if not isinstance(text, str) or not text:
            raise TypeError("название должно быть строкой")
        return text

    def __verify_weight(number):
        """для проверки корректности веса"""
        if not isinstance(number, (int, float)) or number <= 0:
            raise TypeError('вес должен быть положительным числом')
        return number

class Closet(Furniture):
    """для представления шкафов"""
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Chair(Furniture):
    """для представления стульев"""
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return tuple(self.__dict__.values())

class Table(Furniture):
    """для представления столов"""
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return tuple(self.__dict__.values())

f = Furniture("стол", 20)
print(f.__dict__)

cl = Closet('шкаф-купе', 342.56, True, 3)
print(cl.__dict__)
chair = Chair('стул', 14, 55.6)
print(chair.__dict__)
tb = Table('стол', 34.5, 75, 10)
print(tb.__dict__)
print(cl.get_attrs())
print(chair.get_attrs())
print(tb.get_attrs())
