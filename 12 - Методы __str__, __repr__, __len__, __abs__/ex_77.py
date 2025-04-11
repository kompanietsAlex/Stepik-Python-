class Clock:
	def __init__(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def get_time(self): # возвращает текущее время в секундах
		return self.hours * 3600 + self.minutes * 60 + self.seconds

class DeltaClock:
	def __init__(self, clock1, clock2):
		self.clock1 = clock1
		self.clock2 = clock2

	def __len__(self):
		diff = self.clock1.get_time() - self.clock2.get_time()
		return diff if diff > 0 else 0

	def __str__(self):
		diff = self.__len__()
		hours = diff // 3600
		minutes = (diff % 3600) // 60
		seconds = diff % 60
		return f"{hours:02}: {minutes:02}: {seconds:02}"

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400