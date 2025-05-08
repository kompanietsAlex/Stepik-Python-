class IntegerValue:
    # класс дескриптора данных
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        instance.__dict__[self.name] = value

class CellInteger:
    # класс ячейки таблицы
    value = IntegerValue()

    def __init__(self, value=0):
        self.value = value

class TableValues:
    # класс таблицы
    def __init__(self, rows, cols, cell=None):
        if not cell:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    def __getitem__(self, item):
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]].value = value


table = TableValues(10, 10, cell=CellInteger)
print(table[0, 1])

for x in range(1, 10):
    for y in range(1, 10):
        table[x, y] = x * y + 10
# table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()