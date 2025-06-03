class Tuple(tuple):
    def __add__(self, other):
        if hasattr(other, '__iter__'): # проверка, является ли other итерируемым
            return Tuple(super().__add__(tuple(other))) # преобразуем other в кортеж и добавляем к текущему кортежу
        return Tuple(super().__add__((other,))) # добавляем к кортежу другой итерируемый объект или элемент

# Пример использования
t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "OOP"