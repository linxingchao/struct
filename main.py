from link.slink import *

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
    s1 = SinggleLink(0)
    s2 = SinggleLink(1)
    s3 = SinggleLink(3)
    s4 = SinggleLink(4)
    s1.next = s2
    s2.next = s3
    s3.next = s4
    showData(s1)
    head = reserve(s1)
    showData(head)
    