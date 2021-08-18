# 二叉树
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
