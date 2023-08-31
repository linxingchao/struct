import sys

class Package:
    def __init__(self,weights,n,w,maxW):
        self.maxW = maxW
        self.weights = weights #物品重量 [2,2,4,6,3]
        self.n = n #物品个数
        self.w = w  #背包承受的重量
        self.mem = [[False]*10]*5
        
    def package1(self,i,cw): #调用package1(0,0)
        
        if cw == self.w or i == self.n: #cw==w,装满了,i==n,物品都考察完了
            if cw > maxW:
                maxW = cw
            return
        self.package1(i+1,cw) #选择不装第i个物品
        if cw + self.weights[i] < self.w:
            self.package1(i+1,cw+self.weights[i]) #选择装第i个物品
            
    def package2(self,i,cw):
        if cw == self.w or i == self.n:
            if cw > self.maxW:
                self.maxW = cw
            return
        if self.mem[i][cw]: #重复状态
            return
        self.mem[i][cw] = True #记录（i,cw）这个状态
        self.package2(i+1,cw)
        if cw+self.weights[i]<=self.w:
            self.package2(i+1,cw+self.weights[i]) 

#weight:物品重量列表，n：物品个数，w：背包可承载重量
def knapsack(weights,n,w):
    status = [[False]*(w+1)]*n #默认False
    status[0][0] = True #第一行的数据
    if weights[0] <= w:
        status[0][weights[w]] = True
        
    for i in range(1,n): #动态规划状态转移
        for j in range(w+1): #不把第i个物品放入背包
            if status[i-1][j] == True:
                status[i][j] = status[i-1][j]
        for j in range(w-weights[i]+1): #把第i个物品放入背包
            if status[i-1][j] == True:
                status[i][j+weights[i]] = True
                
    for i in range(w,-1,-1): #输出结果
        if status[n-1][i]:
            return i 
    
    return 0     

def knapsack2(items,n,w):
    states = [False]*(w+1)
    states[0] = True
    if items[0]<=w:
        states[items[0]] = True
        
    for i in range(1,n):
        for j in range(w-items[i],-1,-1):
            if states[j] == True:
                states[j+items[i]] = True
                
    for i in range(w,-1,-1):
        if states[i] == True:
            return i
        
    return 0   
         