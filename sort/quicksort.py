
class Merge:
    @staticmethod  
    def merge_sort(arr):
        Merge._merge_sort_c(arr,0,len(arr)-1)
        
    @staticmethod
    def _merge_sort_c(arr:list,p:int,r:int):
        if p >= r:
            return
        q = int((p+r)/2)
        #左边递归
        Merge._merge_sort_c(arr,p,q)
        #右侧递归
        Merge._merge_sort_c(arr,q+1,r)
        #合并
        Merge._merge(arr,p,q,r)

    @staticmethod
    def _merge(arr:list,p:int,q:int,r:int):
        i = p 
        j = q+1
        k = 0
        tmp = [None] * (r - p + 1)
        
        while i <=q and j <=r:
            if arr[i] <= arr[j]:
                tmp[k] = arr[i]
                k = k+1
                i = i+1
            else:
                tmp[k] = arr[j]
                k = k+1
                j = j + 1
                
        #判断剩余区间
        start = i
        end = q
        if j <= r:
            start = j
            end = r
        while start <= end:
            tmp[k] = arr[start]
            k = k + 1
            start = start + 1
        
        #tmp拷贝回arr
        for m in range(len(tmp)):
            arr[p+m] = tmp[m]    
            
 
'''
每一次分区，将分区点放在正确的位置
而且分区点左侧都小于分区点，右侧都大于分区点
'''           
class QuickSort:
    @staticmethod
    def quick_sort(arr):
        QuickSort._q_sort_c(arr,0,len(arr)-1)
    
    @staticmethod
    def _q_sort_c(arr:list,p:int,r:int):
        if p >= r:
            return
        q = QuickSort._partition(arr,p,r)
        QuickSort._q_sort_c(arr,p,q-1)
        QuickSort._q_sort_c(arr,q+1,r)
        
        
    @staticmethod
    def _partition(arr:list,p:int,r:int):
        pivot = arr[r]
        i = p
        for j in range(p,r):
            if arr[j] < pivot:
                arr[i],arr[j] = arr[j],arr[i]
                i = i + 1
        
        arr[i],arr[r] = arr[r],arr[i]
        return i
        