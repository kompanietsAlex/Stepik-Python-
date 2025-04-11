class ShopItem:
	def __init__(self, name, weight, price):
		self.name = name.lower() if type(name) == str else None
		self.weight = weight if type(weight) in (int, float) else None
		self.price = price if type(price) in (int, float) else None

	def __eq__(self, other):
		return self.name == other.name and self.weight == other.weight and self.price == other.price

	def __hash__(self):
		return hash((self.name, self.weight, self.price))

# считывание списка из входного потока
lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']# список lst_in в программе не менять!

shop_items = {}
s = []
for i in lst_in:
	s.append(hash(i))
	n = i.split(":")
	mx = ShopItem(n[0], n[1].split()[0], n[1].split()[1])
	shop_items[mx] = [mx, s.count(hash(i))]
