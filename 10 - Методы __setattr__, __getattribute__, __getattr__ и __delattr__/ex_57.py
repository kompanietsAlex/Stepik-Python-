class Museum:
    def __init__(self, name):
        self.name = name # название музея
        self.exhibits = [] # список экспонатов:

    def add_exhibit(self, obj):
        """добавление нового экспоната в музей"""
        if obj not in self.exhibits: # проверка, не добавлен ли экспонат уже
            self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        """удаление экспоната из музея"""
        if obj in self.exhibits: # проверка, есть ли экспонат в списке
            self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        """получение информации об экспонате"""
        return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"

class Picture:
    def __init__(self,  name, author, descr):
        self.name = name # название
        self.author = author # художник
        self.descr = descr # описание

class Mummies:
    def __init__(self, name, location, descr):
        self.name = name # имя мумии
        self.location = location # место находки
        self.descr = descr # описание

class Papyri:
    def __init__(self, name, data, descr):
        self.name = name # название папируса
        self.data = data # датировка
        self.descr = descr # описание


mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)