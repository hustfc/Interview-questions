class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTowLists(self, list1, list2):
        head = None
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val <= list2.val:
            head = list1
            head.next = self.mergeTowLists(list1.next, list2)
        else:
            head = list2
            head.next = self.mergeTowLists(list1, list2.next)
        return head
    def partition(self, lists, start, end):
        if start == end:
            return lists[start]
        if start < end:
            mid = (start + end) // 2
            l1 = self.partition(lists, start, mid)
            l2 = self.partition(lists, mid + 1, end)
            return self.mergeTowLists(l1, l2)
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        return self.partition(lists, 0, len(lists) - 1)
        # while len(lists) > 1:
        #     list1 = lists.pop()
        #     list2 = lists.pop()
        #     lists.append(self.mergeTowLists(list1, list2))
        #return lists[0]

