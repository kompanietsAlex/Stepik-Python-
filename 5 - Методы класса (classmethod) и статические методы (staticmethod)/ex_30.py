from string import ascii_lowercase, digits

class CardCheck:
	@staticmethod
	def check_card_number(number):
		very_num = 0
		for i_4s in number.split("-"):
			for j_1s in i_4s:
				if j_1s in digits:
					very_num += 1
		return True if very_num == 16 and not " " in number else False

	@staticmethod
	def check_name(name):
		veryfi_name = 0
		for i_4s in name.split(" "):
			for j_1s in i_4s:
				if j_1s in  ascii_lowercase.upper():
					veryfi_name += 1
		return True if veryfi_name + 1 == len(name) else False


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_number)