from random import choices
from string import ascii_lowercase, digits, ascii_uppercase

class EmailValidator:
	def __new__(cls, *args, **kwargs):
		return None

	@classmethod
	def get_random_email(cls): # генерации случайного email адреса
		username = ''.join(choices(ascii_lowercase + digits + ascii_uppercase + "_", k=10))
		return f'{username}@gmail.com'

	@classmethod
	def check_email(cls, email): # True если email записан верно
		if not cls.__is_emaik_str(email):
			return False

		if len(email.split('@')) != 2:
			return False

		if not set(email) < set(ascii_lowercase + digits + ascii_uppercase + '@._-'):
			return False

		if len(email.split('@')[0]) > 100 or len(email.split('@')[1]) > 50:
			return False

		if "." not in email.split('@')[1]:
			return False

		if email.count('..') > 0:
			return False

		return True

	@staticmethod
	def __is_emaik_str(email):
		return type(email) == str