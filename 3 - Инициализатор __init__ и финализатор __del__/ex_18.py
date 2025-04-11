def error_show(func):
	def wrapper(self, *args, **kwargs):
		if self.is_show == False:
			return 'Отображение данных закрыто'
		else:
			return func(self, *args, **kwargs)
	return wrapper



class Graph:
	def __init__(self, data):
		self.data = data
		self.is_show = True

	def set_data(self, data):
		self.data = data

	@error_show
	def show_table(self):
		return ' '.join(map(str, self.data))

	@error_show
	def show_graph(self):
		print(f"Графическое отображение данных: {self.show_table()}")

	@error_show
	def show_bar(self):
		print(f'Столбчатая диаграмма: {self.show_table()}')

	def set_show(self, fl_show):
		self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
print(gr.show_table())