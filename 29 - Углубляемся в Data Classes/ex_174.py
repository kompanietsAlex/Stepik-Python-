from dataclasses import dataclass, field, InitVar

@dataclass
class FontData:

    name: str # название шрифта
    size: float # размер шрифта
    color: int = field(compare=False, default=0) # цвет шрифта с исключением из операций сравнения и значением 0
    type_font: str = field(default=None) # тип шрифта с начальным значением None
    monotype: InitVar[bool] = field(compare=False, default=False) # с исключением из сравнения и значением False

    def __post_init__(self, monotype: bool):
        if not monotype:
            self.type_font = "regular"

font = FontData(name="Tahoma", size=22)
print(font.type_font)