
#每次选出未排序中最大的元素
def bubble_sort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(n):
        flag = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = True
                
        if not flag:
            break
#分为 已排序空间，未排序空间，核心将未排元素插入到已排空间中        
def insert_sort(a,n):
    if n <= 1:
        return
    for i in range(1,n):
        value = a[i]
        #查找插入位置
        for j in range(i-1,-1,-1):
            if a[j] > value:
                a[j+1] = a[j]
            else:
                break
        a[j+1] = value

#与冒泡相反，每次找出未排序中的最小元素      
def selection_sort(a,n):
    if n <= 1:
        return
    
    for i in range(n):
        minValue = a[i]
        for j in (i+1,n):
            minIndex = -1
            if a[j] < minValue:
                minIndex = j
            if minIndex != -1:
                a[i],a[minIndex] = a[minIndex],a[i]
            
        