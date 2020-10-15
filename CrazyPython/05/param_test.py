# 函数的参数

# 关键字参数

print("关键字参数-START")


def girth(width, height):
    print("width:", width)
    print("height", height)
    return 2 * (width + height)


print(girth(3, 4))

# 使用关键字参数传参
print(girth(width=3, height=4))

print(girth(height=4, width=3))

print(girth(3, height=4))

print("关键字参数-END")

print("参数默认值-START")


# 参数默认值


# 为两个参数指定默认值


def say_hi(name="孙悟空", message="欢迎来到疯狂软件"):
    print(name, ",您好")
    print("消息是：", message)


# 全部使用默认参数
say_hi()

# 只有message参数使用默认值
say_hi("白骨精")

# 两个参数都不使用默认值
say_hi("土地爷", "欢迎学习Python")

# 只有name参数使用默认值
say_hi(message="欢迎学习Python")

print("参数默认值-END")

print("--------------")
print("有默认值的，必须在没默认值的后面")


# 定义一个打印三角形的函数，有默认值的参数必须放在后面
def printTriangle(char, height=5):
    for i in range(1, height + 1):
        # 先打印一排空格
        for j in range(height - i):
            print(' ', end='')
        # 再打印一排特殊字符
        for j in range(2 * i - 1):
            print(char, end='')
        print()


printTriangle('@', 6)
printTriangle('#', height=7)
printTriangle(char='*')

print("------")

print("参数收集-个数可变的参数")


# 定义支持参数收集的函数
def test(a, *books):
    print(books)
    # books被当成元祖处理
    for b in books:
        print(b)
    # 输出整数变量a的值
    print(a)


def test2(*books, num):
    print(books)
    # books被当成元祖处理
    for b in books:
        print(b)

    print(num)


# 调用test()函数
test(5, "VUE", "python")
# 给后面的参数传值，必须使用关键字参数
test2("疯狂VUE", "疯狂python", num=20)

print("---------")


def test3(x, y, z=3, *books, **scores):
    print(x, y, z)
    print(books)
    print(scores)


test3(1, 2, 3, "疯狂IOS", "疯狂JAVA", 语文=100, 数学=90)
test3(4, 5, 语文=500, 数学=900)

print("---------")

print("逆向参数收集")


def testlist(name, message):
    print(name, "，你好")
    print("欢迎来到:", message)


my_list = ["猪八戒", "高老庄"]
testlist(*my_list)

print("---------")


def testtuple(name, *nums):
    print(name, "你好")
    print("得到的数值是：", nums)


my_tuple = (1, 3, 4)
testtuple("沙和尚", *my_tuple)

print("---------")


def testdic(book, price, desc):
    print(book, "这本书的价格是：", price)
    print("这本书的描述是：", desc)


my_dict = {"book": "疯狂IOS", "price": "99", "desc": "这是一本好书"}
testdic(*my_dict)

print("---------")




print("---------")

print("---------")
