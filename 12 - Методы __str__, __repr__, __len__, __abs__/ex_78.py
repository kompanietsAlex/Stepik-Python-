class Ingredient:
	def __init__(self, name, volume, measure):
		self.name = name # название ингредиента (строка)
		if type(volume) in (int, float):
			self.volume = volume # объем ингредиента в рецепте (вещественное число)
		self.measure = measure # единица измерения объема ингредиента (строка),

	def __str__(self):
		return f"{self.name}: {self.volume}, {self.measure}"

class Recipe:
	def __init__(self, *args):
		self.ingredients =  list(args)

	def add_ingredient(self, ing): # добавление ингредиента в рецепт
		self.ingredients.append(ing)

	def remove_ingredient(self, ing): # удаление ингредиента по	объекту из рецепта;
		if ing in self.ingredients:
			self.ingredients.remove(ing)

	def get_ingredients(self): # получение кортежа из текущего рецепта.
		return tuple(self.ingredients)

	def __len__(self):
		return len(self.ingredients)

recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3