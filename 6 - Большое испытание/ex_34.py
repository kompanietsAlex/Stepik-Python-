class Router:
	def __init__(self):
		self.buffer = [] # список для хранения принятых от серверов пакетов
		self.servers = {}


	def link(self, server):
		"""присоединения server к роутеру"""
		self.servers[server.ip] = server
		server.router = self

	def unlink(self, server):
		"""отсоединения server от роутера"""
		s = self.servers.pop(server.ip, False)
		if s:
			s.router = None

	def send_data(self):
		"""для отправки всех пакетов Data соответствующим серверам"""
		for d in self.buffer:
			if d.ip in self.servers:
				self.servers[d.ip].buffer.append(d)
		self.buffer.clear()


class Server:
	server_ip = 1
	def __init__(self):

		self.buffer = [] # список принятых пакетов
		self.ip = Server.server_ip # IP - адрес текущего сервера.
		Server.server_ip += 1
		self.router = None

	def send_data(self, data):
		"""для отправки информационного пакета data"""
		if self.router:
			self.router.buffer.append(data)

	def get_data(self):
		"""возвращает список принятых пакетов"""
		b = self.buffer[:]
		self.buffer.clear()
		return b

	def get_ip(self):
		"""возвращает свой IP-адрес"""
		return self.ip


class Data:
	def __init__(self, msg, ip):
		self.data = msg # передаваемые данные(строка)
		self.ip = ip #IP - адрес назначения.


router = Router()
sv_from = Server()
router.link(sv_from)
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()