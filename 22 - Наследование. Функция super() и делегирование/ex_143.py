class StringDigit(str):
    def __init__(self, string):
        super().__init__()
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")
        self.string = string

    def __add__(self, other):
        return StringDigit(self.string + other)

    def __radd__(self, other):
        return StringDigit(other + self.string)


sd = StringDigit("123")
print(sd)  # 123
sd = sd + "456"  # StringDigit: 123456
print(sd)
sd = "789" + sd  # StringDigit: 789123456
print(sd)
sd = sd + "12f"  # ValueError