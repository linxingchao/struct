
def counting_sort(arr):
    n = len(arr)
    if n <= 1:
        return
    
    # 查找数组中的数据范围
    max = arr[0]
    for i in range(1,n):
        if max < arr[i]:
            max = arr[i]
    #计数数组
    c_arr = [0] * (max + 1)
    
    #计算每个元素的个数
    for i in range(n):
        c_arr[arr[i]] += 1
        
    #累加
    for i in range(1,max+1):
        c_arr[i] = c_arr[i-1] + c_arr[i]
    
    tmp = [None] * n
    for i in range(n-1,-1,-1):
        index = c_arr[arr[i]] - 1
        tmp[index] = arr[i]
        c_arr[arr[i]] = c_arr[arr[i]] - 1
        
    for i in range(n):
        arr[i] = tmp[i]