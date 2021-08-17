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
def createLinklistHead(li):
    head = Node(li[0])
    for ele in li[1:]:
        node = Node(ele)
        node.next = head
        head = node
    return head


def printLinklist(li):
    while li:
        print(li.item, end=',')
        li = li.next


# 尾插法
def createLinklistTail(li):
    head = Node(li[0])
    tail = head
    for ele in li[1:]:
        node = Node(ele)
        tail.next = node
        tail = node
    return head


lhead = createLinklistHead([1, 2, 3])
print("头插法数据")
printLinklist(lhead)

ltail = createLinklistTail([3, 4, 1, 2, 6, 7, ])
print("尾插法数据")
printLinklist(ltail)
