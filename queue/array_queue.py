
class ArrayQueue:
    def __init__(self,capacity):
        self._n = capacity
        self._items = [None]*capacity
        self._head = 0
        self._tail = 0
        
    def enqueue(self,item):
        if self._tail == self._n:
            if self._head == 0 :
                return False
            for i in range(self._head,self._tail):
                self._items[i-self._head] = item[i]
            self._tail -= self._head
            self._head = 0
            
        self._items[self._tail] = item
        ++self._tail
        return True
    
    def dequeue(self):
        if self._head == self._tail:
            return None
        ret = self._items[self._head]
        ++self._head
        return ret
        