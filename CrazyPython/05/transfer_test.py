# 函数的参数传递机制


def swap(a, b):
    # 下面代码实现a、b变量的值交换
    a, b = b, a
    print("在swap函数里，a的值是：", a, ";b的值是，", b)


a = 6
b = 9
swap(a, b)
print("交换结束后，变量a的值是：", a, ";变量b的值是：", b)


def swapdict(dw):
    # 下面代码实现a、b变量的值交换
    dw['a'], dw['b'] = dw['b'], dw['a']
    print("在swap函数里，dw['a']的值是：", dw['a'], ";dw['b']的值是，", dw['b'])


dw = {'a': 6, 'b': 9}
swapdict(dw)
print("交换结束后，dw['a']的值是：", dw['a'], ";dw['b']的值是，", dw['b'])


