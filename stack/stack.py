
class Stack:
    def __init__(self,n):
        self._items = [None]*n
        self._count = 0
        self._n = n
        
    def push(self,item):
        if self._count == self._n:
            return False
        self._items.append(item)
        self._count = self._count + 1
        return True
    
    def pop(self):
        if self._count == 0:
            return None
        tmp = self._items.pop()
        self._count = self._count - 1
        return tmp
            