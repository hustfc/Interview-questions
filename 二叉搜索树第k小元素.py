class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.index = 0
    def Tree(self, rootNums):
        root = None
        if self.index < len(rootNums):
            if rootNums[self.index] == None:
                self.index += 1
                return None
            root = TreeNode(rootNums[self.index])
            self.index += 1
            root.left = self.Tree(rootNums)
            root.right = self.Tree(rootNums)
        return root
    def FindKthNum(self, root, k):
        result = None
        if root:
            if result == None:
                result = self.FindKthNum(root.left, k)
            if result == None and k == 1:
                return root.val
            if result == None and k != 1:
                k -= 1
            result = self.FindKthNum(root.right, k)
        return result
    def kthSmallest(self, root, k) -> int:
        Root = self.Tree(root)
        return self.FindKthNum(Root, k)
root = [3,1,None,2,4,None,None]
Root = Solution().Tree(root)
print(Root.val)
print(Root.left.val)
print(Root.left.left.val)
print(Root.right.val)
print(Solution().kthSmallest(root, 1))