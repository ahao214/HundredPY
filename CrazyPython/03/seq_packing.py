# 序列封包和序列解包
# 序列封包，将10、20、30封装成元祖后赋值给vals
vals = 10, 20, 30
print(vals)
print(type(vals))
print(vals[1])

# 序列解包
a_tuple = tuple(range(1, 10, 2))
# 序列解包，将a_tuple元祖的各个元素依次赋值给a b c d e变量
a, b, c, d, e = a_tuple
print(a, b, c, d, e)


a_list = ["kict", "crazy"]
# 序列解包，将a_list序列的各个元素依次赋值给a_str b_str变量
a_str, b_str = a_list
print(a_str, b_str)

# 将1 2 3 依次赋值给a b c
a, b, c = 1, 2, 3
print(a, b, c)

a, b, c = b, c, a
print(a, b, c)



#first second保存前两个元素，rest列表包含剩下的元素
first, second, *rest = range(10)
print(first)
print(second)
print(rest)

#last保存最后一个元素，begin保存剩余的元素
*begin, last = range(10)
print(begin)
print(last)

# first保存第一个元素，last保存最后一个元素，middle保存其他的元素
first, *middle, last = range(10)
print(first)
print(middle)
print(last)