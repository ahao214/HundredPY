# 列表和元祖

# 列表
my_list = ["crazy", "20", "python"]
print(my_list)

# 元祖
my_tuple = ("crazy", "20", "python")
print(my_tuple)


# 通过索引使用元素
a = ("crazy", "20", "my", "python", "ahao")
print(a)
# 访问第一个元素
print("第一个元素：", a[0])
# 访问第二个元素
print("第二个元素：", a[1])
# 访问倒数第一个元素
print("倒数第一个元素：", a[-1])
# 访问倒数第二个元素
print("倒数第二个元素：", a[-2])

print("--子序列--")
# 访问第2到第4(不包含)的所有元素
print(a[1:3])

print(a[-3:-1])

b = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(b)
print(b[2:3])
print(b[2:8:2])