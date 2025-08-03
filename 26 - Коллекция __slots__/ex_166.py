class Note:
    _av = ("до", "ре", "ми", "фа", "соль", "ля", "си")
    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in self._av:
            raise ValueError('недопустимое значение аргумента')
        if key == "_ton" and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, key, value)

class Notes:
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'
    _av = ("до", "ре", "ми", "фа", "соль", "ля", "си")
    __ins = None

    def __new__(cls, *args, **kwargs):
        if cls.__ins is None:
            cls.__ins = super().__new__(cls)
        return cls.__ins

    def __del__(self):
        Notes.__ins = None

    def __init__(self):
        for key, value in zip(self.__slots__, self._av):
            setattr(self, key, Note(value, 0))


    def __getitem__(self, item):
        if not (0 <= item < 7):
            raise IndexError('недопустимый индекс')
        return getattr(self, self.__slots__[item])

notes = Notes()
print(notes[1]._name, notes[1]._ton)