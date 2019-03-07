class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.k = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = None
        if root:
            if result == None and root.left:
                result = self.kthSmallest(root.left, k)
            if result == None and k == 1:
                return root
            if result == None and k != 1:
                k -= 1
            if result == None and root.right:
                result = self.kthSmallest(root.right, k)
        return result
Root = TreeNode(5)
Root.left = TreeNode(3)
Root.left.left = TreeNode(2)
Root.left.right = TreeNode(4)
Root.right = TreeNode(7)
Root.right.left = TreeNode(6)
Root.right.right = TreeNode(8)
print(Solution().kthSmallest(Root, 3).val)
