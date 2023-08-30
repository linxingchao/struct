#暴力查询
def bk():
    pass

#哈希查询
def rk():
    pass

# 坏字符规则，好后缀规则
# a:主串，n：主串长度，b:模式串，m:模式串长度
def bm(a:list,n:int,b:list,m:int):
    bc = [-1] * 256
    generate_bc(b,m,bc)
    i = 0
    while i < n-m :
        j = 0
        for j in range(m-1,-1,-1):
            if a[i+j] != b[j]:
                break
        if j < 0:
            return i
        i = i + (j - bc[ord(a[i+j])])
        
    return -1

def generate_bc(b,m,bc):
    for i in range(256):
        bc[i] = -1
    for i in range(m):
        ascii = ord(b[i])
        bc[ascii] = i