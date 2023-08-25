from link.slink import *
from sort.quicksort import *
from sort.linear_sort import *

def find1(arr:list,n:int, key:str):
    if arr == None or n <= 0:
        return -1
    
    i = 0
    while i<n:
        if arr[i] == key:
            return i
        ++i
        
    return -1

def find2(arr:list,n:int, key:str):
    if arr == None or n <= 0:
        return -1
    
    if (arr[n-1] == key):
        return n-1
    
    tmp = arr[n-1]
    arr[n-1] = key
    i = 0
    while arr[i] != key:
        ++i
    
    arr[n-1] = tmp
    if i == n-1:
        return -1
    else:
        return i

if __name__ == "__main__":
   test = [2,2,5,5,1,1,0,0,7,9,2,10,4]
   counting_sort(test)
   print(test)
    