class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.results = []
    def RecursionFindPath(self, root, expectNumber, result):
        result.append(root.val)
        if root.left == None and root.right == None and sum(result) == expectNumber:
            results.append(result)
        temp = result[:]
        if root.left:
            self.RecursionFindPath(root.left, expectNumber, result)
        result = temp
        if root.right:
            self.RecursionFindPath()
    def FindPath(self, root, expectNumber):