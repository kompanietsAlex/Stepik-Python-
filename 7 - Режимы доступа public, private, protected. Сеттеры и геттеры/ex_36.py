class Money:
	def __init__(self, mn):
		self.__money = 0
		if self.__check_money(mn):
			self.__money = mn

	@classmethod
	def __check_money(cls, money): # проверкa корректности средств в параметре money
		return type(money) == int and 0 <= money

	def set_money(self, money): # передачa нового значения переменной money
		if self.__check_money(money):
			self.__money = money

	def get_money(self): # получениe текущего объема денег
		return self.__money

	def add_money(self, mn): # прибавлениe средств
		self.__money += mn.__money


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()
print(m1)# 100
m2 = mn_2.get_money()
print(m2)# 120