class CPU:
	def __init__(self, name, fr):
		self.name = name
		self.fr = fr

class Memory:
	def __init__(self, name, volume):
		self.name = name
		self.volume = volume

class MotherBoard:
	def __init__(self, name, cpu, *mems):
		self.name = name
		self.cpu = cpu
		self.total_mem_slots = 4
		self.mem_slots = mems[:self.total_mem_slots]


	def get_config(self):
		res = [f'Материнская плата: {self.name}',
			   f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
			   f'Слотов памяти: {len(self.mem_slots)}',
			   f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}"]
		return res


cpu = CPU('Intel', 7400)
memory = Memory('Samsung', 2400)
mb = MotherBoard('Gigabyte', cpu, memory, memory)
print("\n".join([i for i in mb.get_config()]))