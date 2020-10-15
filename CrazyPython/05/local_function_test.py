# 局部函数


def get_math_func(type, nn):
    # 定义一个计算平方的局部函数
    def square(n):
        return n * n

    # 定义一个计算立方的局部函数
    def cube(n):
        return n * n * n

    # 定义一个计算阶乘的局部函数
    def factorial(n):
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result

    # 调用局部函数
    if type == "square":
        return square(nn)
    elif type == "cube":
        return cube(nn)
    else:
        return factorial(nn)


print(get_math_func("square", 3))
print(get_math_func("cube", 3))
print(get_math_func("", 3))

print("--------")


def foo():
    # 局部变量name
    name = "Charlie"

    def bar():
        nonlocal name
        # 访问bar()函数所在foo()函数内的name局部变量
        print(name)
        name = "孙悟空"

    bar()


foo()

