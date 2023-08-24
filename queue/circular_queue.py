
class CircularQueue:
    def __init__(self,capacity):
        self._items = [None] * capacity
        self._head = 0
        self._tail = 0
        self._n = capacity

    def enqueue(self,item):
        if (self._tail + 1) % self._n == self._head:
            return False
        self._items[self._tail] = item
        self._tail = (self._tail + 1) % self._n

    def dequeue(self):
        if self._head == self._tail:
            return None
        ret = self._items[self._head]
        self._head = (self._head + 1) % self._n
        return ret