
num = 0

def count(a,n):
    num = 0 
    merge_sort_counting(a,0,n-1)
    return num

def merge_sort_counting(a,p,r):
    if p>=r:
        return
    q = int((p+r)/2)
    merge_sort_counting(a,p,q)
    merge_sort_counting(a,p+1,r)
    merge(a,p,q,r)
 
def merge(a:list,p,q,r):
    i = p
    j = q+1
    k = 0
    temp = [None] * (r-p+1)
    
    while i<=q and j<=r:
        if a[i]<=a[j]:
            temp[k] = a[i]
            k=k+1
            i=i+1
        else:
            num = num + (q-i+1)
            temp[k] = a[j]
            k=k+1
            j=j+1
            
    while i <= q:
        temp[k]=a[i]
        k=k+1
        i=i+1
    while j <= r:
        temp[k]=a[j]
        k=k+1
        j=j+1
        
    for i in range(r-p+1):
        a[p+i] = temp[i]