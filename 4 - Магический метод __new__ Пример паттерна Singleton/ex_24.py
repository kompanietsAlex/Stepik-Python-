class SingletonFive:
	__instance = None
	count = 0
	def __new__(cls, *args, **kwargs):
		if  cls.count < 7:
			cls.__instance = super().__new__(cls)
			cls.count += 1
		return cls.__instance


	def __init__(self, name):
		self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]