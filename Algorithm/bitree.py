# 二叉树

from collections import deque

class BitreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子


a = BitreeNode("A")
b = BitreeNode("B")
c = BitreeNode("C")
d = BitreeNode("D")
e = BitreeNode("E")
f = BitreeNode("F")
g = BitreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e


# 前序遍历
def preOrder(root):
    if root:
        print(root.data, end=',')
        preOrder(root.lchild)
        preOrder(root.rchild)


preOrder(root)


# 中序遍历
def inOrder(root):
    if root:
        inOrder(root.lchild)
        print(root.data, end=',')
        inOrder(root.rchild)


inOrder(root)


# 后序遍历
def postOrder(root):
    if root:
        postOrder(root.lchild)
        postOrder(root.rchild)
        print(root.data, end=',')


postOrder(root)


# 层次遍历
def levelOrder(root):
    queue=deque()
    queue.append(root)
    while len(queue)>0:
        node=queue.popleft()
        print(node.data,end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


levelOrder(root)