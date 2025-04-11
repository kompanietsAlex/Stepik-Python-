class Car:
	pass


d = {"model": "Тойота",
	 "color": "Розовый",
	 "number": "П111УУ77"}

for k, v in d.items():
	setattr(Car, k, v)

print(Car.__dict__["color"])