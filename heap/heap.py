#堆是满二叉树
class Heap:
    def __init__(self,capacity:int):
        self._a = [None] * (capacity + 1)
        self._n = capacity
        self._count = 0

    #大顶堆
    #先将新元素添加到最后
    def insert(self,data):
        if self._count > self.n:
            return
        self._count = self._count + 1
        self._a[self._count] = data
        i = self._count
        while int(i/2) > 0 and a[i] > a[int(i/2)]:
            self._a[i],self._a[int(i/2)] = self._a[int(i/2)],self._a[i]
            i = int(i/2)

    def remove_max(self):
        if self._count == 0:
            return -1
        self._a[1] = self._a[self._count]
        self._count = self._count - 1
        Heap.heapify(self._a,self._count,1)

    @staticmethod
    def buildHeap(a,n):
        for i in range(int(n/2),0,-1):
            Heap.heapify(a,n,i)

    @staticmethod
    def sort(a,n:int):
        Heap.buildHeap(a,n)
        k = n
        while k > 1:
            a[1],a[k] = a[k],a[1]
            k = k - 1
            Heap.heapify(a,k,1)

    @staticmethod
    def heapify(self,a,n:int,i:int):
        while True:
            maxPos = i
            if 2*i <= n and a[i] < a[i*2]:
                maxPos = i*2
            if 2*i+1 <= n and a[maxPos] < a[i*2+1]:
                maxPos = i*2+1
            if maxPos == i:
                break
            a[i],a[maxPos] = a[maxPos],a[i]
            i = maxPos