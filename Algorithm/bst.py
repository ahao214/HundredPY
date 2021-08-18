# 二叉搜索树

class BitreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, val):
        if not node:
            node = BitreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:  # 空树
            self.root = BitreeNode(val)
            return

        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BitreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BitreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    # node是叶子结点
    def __remove_node_1(self, node):
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:  # node是它父亲的左孩子
            node.parent.lchild = None
        else:  # node是它父亲的右孩子
            node.parent.rchild = None

    # node只有一个左孩子
    def __remove_node_21(self, node):
        # node只有一个左孩子
        if not node.parent:  # 根结点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    # node只有一个右孩子
    def __remove_node_22(self, node):
        if not node.parent: # 根结点
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent



