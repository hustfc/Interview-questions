class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        nextNode = head.next
        nextNode.next = self.swapPairs(nextNode.next)
        head.next = nextNode.next
        nextNode.next = head
        return nextNode