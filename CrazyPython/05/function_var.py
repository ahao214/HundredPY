# 使用函数变量


# 定义一个计算乘方的函数
def pow(base, exponent):
    result = 1
    for i in range(1, exponent + 1):
        result *= base
    return result


# 将pow函数赋值给my_func，则my_func可被当成pow使用
my_func = pow

print(my_func(3, 4))


# 定义一个计算面积的函数
def area(width, height):
    return width * height


my_func = area
print(my_func(4, 5))

print("使用函数作为函数形参")


# 定义函数类型的形参，其中fn是一个函数
def map(data, fn):
    result = []
    # 遍历data列表中的每个元素，并用fn函数对每个元素进行计算
    # 然后将计算结果作为新数组的元素
    for e in data:
        result.append(fn(e))
    return result


# 定义一个计算平方的函数
def square(n):
    return n * n


# 定义一个计算立方的函数
def cube(n):
    return n * n * n


# 定义计算一个阶乘的函数
def factorial(n):
    result = 1
    for index in range(2, n + 1):
        result *= index
    return result


data = [3, 4, 9, 5, 8]

print("原数据：", data)

# 下面程序代码调用map()函数三次，每次调用时传入不同的函数
print("计算数组元素的平方")
print(map(data, square))

print("计算数组元素的立方")
print(map(data, cube))

print("计算数组元素的阶乘")
print(map(data, factorial))

print(type(map))


print("-------")


print("使用函数作为返回值")


def get_math_func(type):
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

    # 返回局部函数
    if type == "square":
        return square
    if type == "cube":
        return cube
    else:
        return factorial


math_func = get_math_func("square")
print(math_func(5))

math_func = get_math_func("cube")
print(math_func(5))

math_func = get_math_func("factorial")
print(math_func(5))
