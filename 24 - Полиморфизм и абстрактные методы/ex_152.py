class ShopInterface:
    def get_id(self):
        """Возвращает идентификатор магазина."""
        raise NotImplementedError('в классе не переопределен метод get_id')

class ShopItem(ShopInterface):

    __id = 0

    def __init__(self, name, weight, price):
        """Инициализирует товар с заданными параметрами"""
        self._name = name # Название товара
        self._weight = weight # Вес товара
        self._price = price # Цена товара
        self.__id = self.__class__.__id
        self.__class__.__id += 1

    def get_id(self):
        """Возвращает идентификатор товара."""
        return self.__id

item1 = ShopItem("имя1", "вес1", "100")
item2 = ShopItem("имя2", "вес2", "200")
print(item1.get_id())
print(item2.get_id())