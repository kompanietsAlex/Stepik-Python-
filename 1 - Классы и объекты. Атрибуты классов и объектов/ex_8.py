class Person:
	name = 'Сергей Балакирев'
	job = 'Программист'
	city = 'Москва'


p1 = Person()
print(Person.__dict__)
print(p1.__dict__)
print(True if "job"in p1.__dict__ else False)