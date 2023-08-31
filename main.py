from link.slink import *
from sort.quicksort import *
from sort.linear_sort import *
from graph import Graph
from reduce import *

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
   g = Graph(8)
   g.add_edge(0,1)
   g.add_edge(0,3)
   g.add_edge(1,2)
   g.add_edge(1,4)
   g.add_edge(2,5)
   g.add_edge(3,4)
   g.add_edge(4,5)
   g.add_edge(4,6)
   g.add_edge(5,7)
   g.add_edge(6,7)
   g.bfs(0,5)
    