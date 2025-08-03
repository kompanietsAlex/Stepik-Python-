from dataclasses import dataclass

@dataclass(init=False, repr=False)
class Volume:

    height: int # высота
    width: int # ширина
    depth: int # глубина

    def get_volume(self ):
        """Возвращает объем"""
        return self.height * self.width * self.depth

v = Volume()
v.height = 10
v.width = 20
v.depth = 30
res = v.get_volume()