# 链表

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

#
# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c
# print(a.next.item)
# print(b.next.item)


# 头插法
def createLinklist(li):
    head = Node(li[0])
    for ele in li[1:]:
        node = Node(ele)
        node.next = head
        head = node
    return head


lk=createLinklist([1,2,3])
print(lk.item)
print(lk.next.item)
