class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}
        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        del self.tr[eng]

    def translate(self, eng):
        return self.tr[eng]

tr = Translator()

lst = ["tree-дерево", "car-машина", "car-автомобиль",
       "leaf-лист", "river-река", "go-идти",
       "go-ехать", "go-ходить", "milk-молоко"]
for i in lst:
    tr.add(i.split("-")[0], i.split("-")[1])

tr.remove("car")

print(*tr.translate("go"))