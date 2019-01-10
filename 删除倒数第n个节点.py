class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None or n < 1:
            return None
        p = head
        for i in range(n):
            p = p.next
        #如果p为None，那么需要删除头结点
        if p == None:
            tempHead = head
            head = head.next
            del tempHead
            return head
        preNode = head
        while p.next:
            preNode = preNode.next
            p = p.next
        deleteNode = preNode.next
        preNode.next = deleteNode.next
        del deleteNode
        return head
