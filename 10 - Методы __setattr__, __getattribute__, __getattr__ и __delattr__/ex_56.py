class Course:
	"""класс, отвечающий за управление курсом в целом;"""
	def __init__(self, name):
		self.name = name # название курса(строка)
		self.modules = [] # список модулей курса

	def add_module(self, module):
		"""добавление нового модуля в конце списка modules"""
		self.modules.append(module) # добавляем модуль в конец списка modules

	def remove_module(self, indx):
		"""удаление модуля из списка modules по индексу в этом списке"""
		self.modules.pop(indx)


class Module:
	"""класс, описывающий один модуль (раздел) курса;"""
	def __init__(self, name):
		self.name = name # название модуля(строка)
		self.lessons = [] # список уроков модуля

	def add_lesson(self, lesson):
		"""добавление в модуль нового урока LessonItem"""
		self.lessons.append(lesson) # добавляем урок в конец списка lessons

	def remove_lesson(self, indx):
		"""удаление урока по индексу в списке lessons"""
		self.lessons.pop(indx)


class LessonItem:
	"""класс одного занятия (урока)"""
	attrs = {"title": str, "practices": int, "duration": int}
	def __init__(self, title, practices, duration):
		self.title = title # название урока(строка)
		self.practices = practices # число практических занятий
		self.duration = duration # общая длительность урока

	def __setattr__(self, key, value):
		if key in self.attrs:
			if type(value) != self.attrs[key]:
				raise TypeError("Неверный тип присваиваемых данных.")
			if (key == "practices" or key == "duration") and value <= 0:
				raise TypeError("Неверный тип присваиваемых данных.")

		super().__setattr__(key, value)

	def __getattr__(self, item):
		return False

	def __delattr__(self, item):
		if item in self.attrs:
			raise AttributeError()

		super().__delattr__(item)

course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)