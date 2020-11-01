class Cat:
    def __init__(self, name):
        self.name = name


def walk_func(self):
    print('%s慢慢走过一片草地' % self.name)


d1 = Cat('Garfield')
d2 = Cat('Kitty')

# 为Cat动态添加walk()方法，该方法第一个参数会自动绑定
Cat.walk = walk_func()

# 调用d1和d2的walk()方法
d1.walk()
d2.walk()
