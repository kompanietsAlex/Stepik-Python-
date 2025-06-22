class SoftList(list):
    def __getitem__(self, index):
        if 0 <= abs(index) < len(self):
            return super().__getitem__(index)
        return False

sl = SoftList("python")
print(sl[0]) # 'p'
print(sl[-1]) # 'n'
print(sl[6]) # False
print(sl[-7]) # False