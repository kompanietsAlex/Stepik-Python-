from abc import ABC, abstractmethod
class Model(ABC):
    @abstractmethod
    def get_pk(self):
        """возвращает первичный ключ модели"""
        pass

    def get_info(self):
        """возвращает информацию о модели"""
        return f"Базовый класс Model"

class ModelForm(Model):
    _id = 0
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.__class__._id
        self.__class__._id += 1

    def get_pk(self):
        """возвращает первичный ключ модели"""
        return self._id

form = ModelForm("Логин", "Пароль")
print(form.get_pk())
