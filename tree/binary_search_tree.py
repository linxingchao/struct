from tree import TreeNode

class BinarySearchTree:
    def __init__(self,node:TreeNode):
        self.root = node
        
    def find(self,data)->TreeNode:
        p = self.root
        while p != None:
            if data < p.data:
                p = p.left
            elif data > p.data:
                p = p.right
            else:
                return p
        return None
    
    '''
    新元素为叶子节点
    '''
    def insert(self,data):
        if self.root == None:
            self.root = TreeNode(data)
            return
        p = self.root
        while p != None:
            if data > p.data:
                if p.right == None:
                    p.right = TreeNode(data)
                    return
                p = p.right
            else:
                if p.left == None:
                    p.left = TreeNode(data)
                    return
                p = p.left

    '''
    1.删除元素为叶子节点
    2.删除元素只有一个子节点
    3.删除元素有两个子节点，使用右子树中，最小节点来替换删除节点

    '''
    def delete(self,data):
        p = self.root #要删除的节点
        pp = None #记录p的父节点
        #查询删除节点位置
        while p != None and p.data != data {
            pp = p
            if data > p.data:
                p = p.right
            else:
                p = p.left
        }
        #没有找到
        if p == None:
            return 

        #删除的节点有两个子节点
        if p.left != None and p.right != None:
            min_p = p.right
            min_pp = p
            while min_p.left != None {
                min_pp = min_p
                min_p = min_p.left
            }
            p.data = min_p.data
            p = min_p
            pp = min_pp

        #删除节点是叶子节点或仅有一个节点
        child = None
        if p.left is not None:
            child = p.left
        elif p.right != None:
            child = p.right
        
        if pp == None:
            self.root = child
        elif pp.left == p:
            pp.left = child
        else pp.right = child

    def delete1(self,value):
        p = self.root
        pp = None
        #查找到需要删除的节点
        while p is not None and p.data != value:
            pp = p
            if p.data > value:
                p = p.left
            else:
                p = p.right

        if p is None:
            return

        #删除元素有两个子节点
        if p.left is not None and p.right is not None:
            min_p = p.right
            min_pp = p 
            while min_p.left is not None:
                min_pp = min_p
                min_p = min_p.left
            
            #数据交换，将需要删除的节点数据，交换到叶子节点，然后删除叶子节点
            p.data = min_p.data
            p = min_p
            pp = min_pp
   
        #删除节点是叶子节点或仅有一个节点
        child = None
        if p.left is not None:
            child = p.left
        elif p.right != None:
            child = p.right
        
        if pp == None:
            self.root = child
        elif pp.left == p:
            pp.left = child
        else:
            pp.right = child          
                
        