#暴力查询
def bk():
    pass

#哈希查询
def rk():
    pass

# 坏字符规则，好后缀规则
# a:主串，n：主串长度，b:模式串，m:模式串长度
def bm(a:list,n:int,b:list,m:int):
    bc = [-1] * 256 #记录模式串中每个字符最后出现的位置
    generate_bc(b,m,bc) #构建坏字符哈希表
    i = 0  # i表示主串与模式串对其的第一个字符
    while i < n-m :
        j = 0
        for j in range(m-1,-1,-1): #模式串从后往前匹配
            if a[i+j] != b[j]: #坏字符对应模式串中的下表是j
                break
        if j < 0:
            return i #匹配成功，返回主串与模式串第一个匹配的字符的位置
        #这里等于将模式串往后滑动j-bc[ord(a[i+j])]位
        #bc存储模式串中，字符位置
        i = i + (j - bc[ord(a[i+j])])
        
    return -1

def generate_bc(b,m,bc):
    for i in range(256):
        bc[i] = -1
    for i in range(m):
        ascii = ord(b[i])
        bc[ascii] = i
        
#b:模式串，m长度，suffix        
def generateGS(b,m,suffix,prefix):
    suffix = [-1] * m
    prefix = [False]*m
    for i in range(m-1):
        j = i
        k = 0
        while j >= 0 and b[j] == b[m-1-k]:
            j = j-1
            k = k +1
            suffix[k] = j + 1
        if j == -1:
            prefix[k] = True
        