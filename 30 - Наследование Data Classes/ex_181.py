from dataclasses import make_dataclass, field

Window = make_dataclass(
    "Window", ["width", "height", ("color",str, field(default= 'gray'))],
             namespace={"draw": lambda self: f"window: {(self.width, self.height)}; color: {self.color}"})
wnd = Window(100, 20)
print(wnd.draw())