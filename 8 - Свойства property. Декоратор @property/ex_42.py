class Car:
	def __init__(self, model):
		self.__modul = model

	@property
	def model(self):
		return self.__modul

	@model.setter
	def model(self, model):
		if type(model) is str and 2 <= len(model) <= 100:
			self.__modul = model


car = Car('Tesla Model S')
car.model = 56
print(car.model)