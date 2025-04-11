class Body:
	def __init__(self, name, ro, volume):
		self.name = name # название тела
		self.ro = ro # плотность тела
		self.volume = volume # объем тела

	def calculate_mass(self):
		return self.ro * self.volume

	def __lt__(self, other):
		if type(other) == int:
			return self.calculate_mass() < other
		else:
			return self.calculate_mass() < other.calculate_mass()

	def __eq__(self, other):
		if type(other) == int:
			return self.calculate_mass() == other
		else:
			return self.calculate_mass() == other.calculate_mass()


body1 = Body('Cube', 1, 100)
body2 = Body('Cube', 1, 200)
body3 = Body('Cube', 2, 50)

print(body1 > body2)  # True, если масса тела body1 больше массы тела body2
print(body1 == body2) # True, если масса тела body1 равна массе тела body2
print(body1 < 10)     # True, если масса тела body1 меньше 10
print(body2 == 5)     # True, если масса тела body2 равна 5