# 21. 合并两个有序链表


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        cur = res
        while(l1 != None and l2 != None):
            if l1.val<=l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return res.next