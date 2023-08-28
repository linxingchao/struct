from tree import TreeNode

def pre_order(root:TreeNode):
    if root == None:
        return 
    print(root.data)
    pre_order(root.left)
    pre_order(root.right)

def in_order(root:TreeNode):
    if root == None:
        return
    in_order(root.left)
    print(root.data)
    in_order(root.right)
    
def post_order(root:TreeNode):
    if root == None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data)