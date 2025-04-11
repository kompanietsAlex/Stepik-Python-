class Model:
	def query(self, *args, **kwargs):
		for k, v in kwargs.items():
			setattr(self, k, v)


	def __str__(self):
		t = [f"{k}={str(v)}" for k, v in self.__dict__.items()]
		if t:
			return f'{self.__class__.__name__}: {", ".join(t)}'
		else:
			return f'{self.__class__.__name__}'

model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)