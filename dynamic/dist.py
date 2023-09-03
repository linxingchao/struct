import sys
import math

matrix = [[1,3,5,9],
          [2,1,3,4],
          [5,2,6,7],
          [6,8,4,3]]

class Dist:
    def __init__(self,n,matrix):
        self.min_dist = sys.maxsize
        self.n = n
        self.mem = [[-1]*n]*n
        self.matrix = matrix
    
    # i，j：矩阵行列位置，dist当前走过额距离，w矩阵，n矩阵行列大小n*n
    def min_distBT(self,i,j,dist,w,n): #无状态记录
        if i == n and j == n:
            if dist < self.min_dist:
                self.min_dist = dist
                return
        if i<n: #往下走
            self.min_distBT(i+1,j,dist+w[i][j],w,n)
        if i < n:
            self.min_dist(i,j+1,dist+w[i][j],w,n)
    
    def mini_distDP(self,martix,n):
        states = [[0]*n]*n
        sum = 0
        for j in range(n):
            sum += martix[0][j]
            states[0][j] = sum
        sum = 0
        for i in range(n):
            sum += martix[i][0]
            states[i][0] = sum
            
        for i in range(1,n):
            for j in range(1,n):
                states[i][j] = martix[i][j] + min(states[i][j-1],states[i-1][j])
        
        return states[n-1][n-1]
            
            
    def min_dist(self,i,j):
        if i==0 and j==0:
            return self.matrix[0][0]
        if self.mem[i][j]>0:
            return self.mem[i][j]
        min_left = sys.maxsize
        if j-1>=0:
            min_left = self.min_dist(i,j-1)
        min_up = sys.maxsize
        if i-1>=0:
            min_up = self.min_dist(i-1,j)
        cur_min_dist = self.matrix[i][j] + min(min_left,min_up)
        self.mem[i][j] = cur_min_dist
        return cur_min_dist