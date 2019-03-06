class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

def leftView(root, level, alist):
    print(root)
    if root == None:
        return
    if level == len(alist):
        alist.append(root.val)
    leftView(root.left, level+1, alist)
    leftView(root.right, level+1, alist)

def View(root):
    left, right = [], []
    leftView(root, 0, left)
    #rightView(root, 0, right)
    print(left)
    #print(right)

View(root)




