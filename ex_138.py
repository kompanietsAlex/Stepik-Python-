class Thing:
    def __init__(self, name, weight):
        self.name = name # наименование предмета (строка)
        self.weight = weight # вес предмета (вещественное число)

class ArtObject(Thing):
    """для представления арт-объектов"""
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = author
        self.date = date

class Computer(Thing):
    """для системных блоков компьютеров"""
    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.cpu = cpu  # процессор
        self.memory = memory  # оперативная память

class Auto(Thing):
    """для автомобилей"""
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims # габариты автомобиля (кортеж из трех чисел: длина, ширина, высота)

class Mercedes(Auto):
    """для автомобилей марки Mercedes"""
    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = model  # модель автомобиля
        self.old = old # возраст автомобиля (в годах)

class Toyota(Auto):
    """для автомобилей марки Toyota"""
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = model  # модель автомобиля
        self.wheel = wheel  # количество колес автомобиля