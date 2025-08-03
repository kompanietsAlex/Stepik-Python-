from dataclasses import dataclass

@dataclass
class Person:

    fio: str # фамилия, имя, отчество
    old: int # возраст
    salary: int = 0 # зарплата, с нулевым начальным значением