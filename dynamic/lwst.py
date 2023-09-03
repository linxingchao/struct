import sys

#莱文斯坦
class LEST:
    def __init__(self,a,b):
        self.str_a = a
        self.str_b = b
        self.n = len(a)
        self.m = len(b)
        self.min_dist = sys.maxsize
         
    # 调用方式 lwst_bt(0,0,0)
    def lwst_bt(self,i,j,edist):
        if i == self.n or j == self.m:
            if i<self.n:
                edist += (self.n-i)
            if j<self.m:
                edist += (self.m-j)
            if edist < self.min_dist:
                self.min_dist=edist
            return
        
        if self.str_a[i] == self.str_b[j]:#两个字符匹配
            self.lwst_bt(i+1,j+1,edist)
        else: #两个字符不匹配
            self.lwst_bt(i+1,j,edist+1) #删除str_a[i]或者b[j]前添加一个字符
            self.lwst_bt(i,j+1,edist+1) #删除b[j]或者a[i]前添加一个字符
            self.lwst_bt(i+1,j+1,edist+1)#将a[i]和b[j]替换为相同的字符