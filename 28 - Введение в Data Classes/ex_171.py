from dataclasses import dataclass, field
@dataclass
class Student:
    """Класс для представления студента."""

    fio: str # фамилия, имя, отчество)
    group: str # группа
    marks: list = field(default_factory=list)# оценки студента

    def __repr__(self):
        """Возвращает строковое представление студента."""
        return f"Студент: {self.fio}, Группа: {self.group}, Оценки: {self.marks}"

s1 = Student("Ганди Индира", "МГИМО-11", [5, 4, 3])
print(s1)
s2 = Student("Манделла Нельсон", "МГИМО-32")
print(s2)