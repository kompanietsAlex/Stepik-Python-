class Animal:
    def __init__(self, name, kind, old):
        self.__name = name # название животного
        self.__kind = kind # вид животного
        self.__old = old # возраст животного

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind):
        self.__kind = kind

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old


animals = [Animal("Васька", "дворовый кот", 5),
           Animal("Рекс", "немецкая овчарка", 8),
           Animal("Кеша", "попугай", 3)]