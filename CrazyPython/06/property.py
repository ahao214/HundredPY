# 使用property函数定义属性


class Rectangel:
    # 定义构造方法
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 定义setsize()函数
    def setsize(self, size):
        self.width, self.height = size

    # 定义getsize()函数
    def getsize(self):
        return self.width, self.height

    # 定义delsize()函数
    def delsize(self):
        self.widht, self.height = 0, 0

    # 使用property定义属性
    size = property(getsize, setsize, delsize, '用于描述矩形大小的属性')


# 访问size属性的说明文档
print(Rectangel.size.__doc__)
# 通过内置的help()函数查看Rectangle.size的说明文档
help(Rectangel.size)
rect = Rectangel(4, 3)

# 访问rect的size属性
print(rect.size)

# 对rect的size属性赋值
rect.size = 9, 7
# 访问rect的width、height实例变量
print(rect.width)
print(rect.height)


# # 删除rect的size属性
# del rect.size
#
# # 访问rect的width、height实例变量
# print(rect.width)
# print(rect.height)


class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def getfullname(self):
        return self.first + ',' + self.last

    def setfullname(self, fullname):
        first_last = fullname.rsplit(',')
        self.first = first_last[0]
        self.last = first_last[1]

    # 使用property()函数定义fullname属性，只传入两个参数
    # 该属性是一个读写属性，但不能删除
    fullname = property(getfullname, setfullname)


u = User('悟空', '孙')

# 访问fullname属性
print(u.fullname)

# 对fullname属性赋值
u.fullname = '八戒,猪'
print(u.first)
print(u.last)
