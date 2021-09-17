# 24. 两两交换链表中的节点

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        res = ListNode()
        res.next = head
        cur = res
        while cur.next is not None and cur.next.next is not None:
            nxt = head.next
            tmp = nxt.next
            cur.next = nxt
            nxt.next = head
            head.next = tmp
            cur = head
            head = head.next
        return res.next


    # 递归方法
    def swapPair(self,head:ListNode)->ListNode:
        if head is None or head.next is None:
            return head
        nxt = head.next
        head.next = self.swapPair(head.next.next)
        nxt.next = head
        return nxt
