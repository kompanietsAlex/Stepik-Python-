from random import randint

class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0

class TicTacToe:
    def __init__(self):
        self._size = 3
        self._win = 0 # 0 - игра; 1 - победа человека; 2 - победа компьютера; 3 - ничья
        self.pole = tuple(tuple(Cell() for _ in range(self._size)) for _ in range(self._size))

    def __check_index(self, index):
        if type(index) not in (tuple, list) or len(index) != 2:
            raise IndexError('некорректно указанные индексы')
