class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != float or not(self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')

class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if type(value) != int or not(self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


def is_valid(lst, validators):
    res = []
    for x in lst:
        for v in validators:
            try:
                v(x)
                res.append(x)
                break  # Если значение прошло валидацию, выходим из цикла
            except ValueError:
                pass
    return res

fv = FloatValidator(0, 10.5)
fv(5.5)  # True
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]