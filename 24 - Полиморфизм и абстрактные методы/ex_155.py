from abc import ABC, abstractmethod
class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass

class Stack(StackInterface):
    def __init__(self, top=None):
        self._top = top

    def push_back(self, obj):
        if self._top == None:
            self._top = obj
        else:
            obj._next = self._top
            self._top = obj

    def pop_back(self):
        if self._top == None:
            return None
        else:
            obj = self._top
            self._top = self._top._next
            return obj

class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None


st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back()