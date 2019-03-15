class Solution:
    def listLength(self, head):
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        return length
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        k = k % (self.listLength(head))
        if k == 0:
            return head
        p = head
        for i in range(k):
            p = p.next
        newHead = head
        while p:
            p = p.next
            newHead = newHead.next
        p = newHead
        while p.next:
            p = p.next
        p.next = head
        p = head
        while p.next != newHead:
            p = p.next
        p.next = None
        return newHead