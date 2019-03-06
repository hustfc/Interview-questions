class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def ReverseList(head):
    if head == None:
        return None
    p = head
    newHead = None
    while p:
        print(p.val)
        nextNode = p.next
        p.next = newHead
        newHead = p
        p = nextNode
    return newHead
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
newHead = ReverseList(head)
print(newHead.val)
print(newHead.next.val)
print(newHead.next.next.val)