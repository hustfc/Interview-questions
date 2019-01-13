class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        listNode = []
        p = head
        for i in range(k):
            listNode.append(p)
            p = p.next
            if i < k - 1 and p == None:
                return head
        newHead = listNode[k - 1]
        newHeadNext = self.reverseKGroup(newHead.next, k)
        print('#', newHead.next.val)
        for i in range(k - 1, 0, -1):
            listNode[i].next = listNode[i - 1]
        listNode[0].next = newHeadNext
        return newHead
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
newHead = Solution().reverseKGroup(l1, 2)
print(newHead.val)
print(newHead.next.val)
print(newHead.next.next.val)
print(newHead.next.next.next.val)