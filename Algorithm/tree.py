class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type  # 'dir' or 'file'
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self, name):
        return self.now.children

    # def cd(self, name):


tree = FileSystemTree()
tree.mkdir("var/")
print(tree.root.children)
