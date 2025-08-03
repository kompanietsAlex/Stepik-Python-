from dataclasses import dataclass

@dataclass()
class House:

    addr: str # адрес дома
    size: float # площадь дома
    floors: int = 1 # число этажей
    rooms: int = 3  # число комнат

    def __eq__(self, other):
        return (self.floors, self.rooms) == (other.floors,  other.rooms)

h1 = House( "Москва, ул. Тверская, д. 5", 102.5, 3, 7)
h2 = House("Москва, ул. Воздвиженка, д. 11", 82.3, 2, 6)
print(h1 == h2)