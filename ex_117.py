class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio # ФИО сотрудника (строка)
        self.job = job # наименование должности (строка)
        self.old = old # возраст (целое число)
        self.salary = salary # зарплата (число: целое или вещественное)
        self.year_job = year_job # непрерывный стаж на указанном месте работы (целое число).
        self.attrs = tuple(self.__dict__) # атрибуты класса
        self.len_attrs = len(self.attrs) # количество атрибутов класса
        self.iter_index = -1

    def check_index(self, index):
        if type(index) != int or not (-self.len_attrs <= index < self.len_attrs):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_index(item)
        return getattr(self, self.attrs[item])

    def __setitem__(self, key, value):
        self.check_index(key)
        setattr(self, self.attrs[key], value)

    def __iter__(self):
        self.iter_index = -1
        return self

    def __next__(self):
        if self.iter_index < self.len_attrs - 1:
            self.iter_index += 1
            return getattr(self, self.attrs[self.iter_index])
        raise StopIteration

# Пример использования класса
pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
print(pers.attrs)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError