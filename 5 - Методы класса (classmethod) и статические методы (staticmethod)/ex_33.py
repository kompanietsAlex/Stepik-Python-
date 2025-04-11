class Message:
	def __init__(self, text, fl_like=False):
		self.text = text
		self.fl_like = fl_like


class Viber:
	messages_box = []

	@classmethod
	def add_message(cls, msg):
		"""добавление нового сообщения в список сообщений"""
		cls.messages_box.append(msg)

	@classmethod
	def remove_message(cls, msg):
		"""удаление сообщения из списка"""
		cls.messages_box.remove(msg)

	@classmethod
	def set_like(cls, msg):
		"""поставить/убрать лайк для сообщения msg"""
		if cls.messages_box[cls.messages_box.index(msg)].fl_like == False:
			cls.messages_box[cls.messages_box.index(msg)].fl_like = True
		else:
			cls.messages_box[cls.messages_box.index(msg)].fl_like = False

	@classmethod
	def show_last_message(cls, number):
		"""отображение последних сообщений"""
		for m in cls.messages_box[-number:]:
			print(m.__dict__["text"])

	@classmethod
	def total_messages(cls):
		"""возвращает общее число сообщений"""
		return len(cls.messages_box)



m = Message("Всем привет!")
Viber.add_message(m)
Viber.show_last_message(1)
