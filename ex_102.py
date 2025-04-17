import sys
class MailBox:
	def __init__(self):
		self.inbox_list = []

	def receive(self):
		# Получаем список писем
		lst_in = list(map(str.strip, sys.stdin.readlines()))
		# Преобразуем каждую строку в объект MailItem
		for i in lst_in:
			self.inbox_list.append(MailItem(*i.split("; ")))

class MailItem:
	def __init__(self, mail_from, title, content):
		self.mail_from = mail_from # Отправитель
		self.title = title # Заголовок письма
		self.content = content # Содержимое письма
		self.is_read = False # По умолчанию письмо не прочитано

	def set_read(self, fl_read):
		# Устанавливаем статус прочтения
		self.is_read = fl_read

	def __bool__(self):
		# Письмо считается "пустым", если оно прочитано
		return self.is_read

# Пример использования
mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(lambda x: bool(x), mail.inbox_list))
print(list(i.__dict__ for i in inbox_list_filtered))

# lst_in = ["sc_lib@list.ru; От Балакирева; Успехов в IT!",
# 		          "mail@list.ru; Выгодное предложение; Вам одобрен кредит.",
# 				  "mail123@list.ru; Розыгрыш; Вы выиграли 1 млн.руб. Переведите 30 тыс.руб., чтобы его получить."]