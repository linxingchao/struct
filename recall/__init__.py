
#results = [0] * 8 #下标表示行，表示queen在哪一列
#count_test = 0

class Queen:
    def __init__(self):
        self._results = [0] * 8
        self._count = 0
    
    @property
    def count(self):
        return self._count
        

    def cal8queeens(self,row):
        #count = 0
        if row == 8:
            self.print_queens(self._results)
            self._count += 1
            return
        for column in range(8):
            if self.is_ok(row,column): #
                self._results[row] = column #第row行的棋子放在第column列
                self.cal8queeens(row+1) #考察下一行


    def print_queens(self,results):
        for row in range(8):
            for column in range(8):
                if results[row] == column:
                    print("Q ",end="")
                else:
                    print("* ",end="")
            print()
        print()
        
    # 判断row行column列放置是否合适    
    def is_ok(self,row,column):
        leftup = column - 1
        rightup = column + 1
        for i in range (row-1,-1,-1): #逐行往上考察每一行
            if self._results[i] == column: #第i行的column是否有棋子
                return False
            if leftup >= 0: #考察左上对角线
                if self._results[i] == leftup:
                    return False
            if rightup < 8: #考察右上对角线
                if self._results[i] == rightup:
                    return False
            leftup = leftup - 1
            rightup = rightup + 1
        return True