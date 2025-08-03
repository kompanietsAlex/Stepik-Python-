from dataclasses import dataclass, field

@dataclass
class Velocity:

    model: str = field(compare=False) # с исключением из операций сравнения
    speed: float = field(init=False, default=0) #с исключением из параметров инициализатора и начальным значением 0
    weight: float # вес
    dims: tuple = field(compare=False, repr=False, default=None)# исключением  сравнения и метода repr и значением None

vl1 = Velocity(model="car", weight=5.4, dims=(100, 20, 30))
vl2 = Velocity(model="ship", weight=5.4, dims=(500, 200, 130))
res = vl1 == vl2  # сравнение объектов
print(res)  # вывод результата сравненияA