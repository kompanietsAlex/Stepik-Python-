from random import randint

class RandomPassword:
	def __init__(self, psw_chars, min_length, max_length):
		self.psw_chars = psw_chars # строка	из разрешенных в пароле	символов;
		self.min_length, self.max_length = min_length, max_length # мин и макс длина паролей.

	def __call__(self):
		length = randint(self.min_length, self.max_length)
		return ''.join(self.psw_chars[randint(0, len(self.psw_chars) - 1)] for _ in range(length))

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)
psw = rnd()
lst_pass = [rnd() for _ in range(3)]