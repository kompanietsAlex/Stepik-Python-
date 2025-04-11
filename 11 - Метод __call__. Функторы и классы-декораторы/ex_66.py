class RenderList:
	def __init__(self, type_list):
		self.type_list = "ol" if type_list == "ol" else "ul"


	def __call__(self, items):
		html = f"<{self.type_list}>"
		for item in items:
			html += f" <li>{item}</li>"
		html += f" </{self.type_list}>"
		return html

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)