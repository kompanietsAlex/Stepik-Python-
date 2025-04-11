class FileAcceptor:
	def __init__(self, *args):
		self.extensions = list(args)

	def __add__(self, other):
		return FileAcceptor(*(self.extensions + other.extensions))

	def __call__(self, s, *args, **kwargs):
		if isinstance(s, str) and '.' in s:
			indx = s.rfind('.')
			return [False, True][s[indx + 1:] in self.extensions]


acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2