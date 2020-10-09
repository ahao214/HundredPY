count_i = 0
while count_i < 5:
    print("count_i小于5：", count_i)
    count_i += 1
else:
    print("count_i大于或等于5")

a_list = [2, 23, "it", -3.5, 56]
for ele in a_list:
    print("元素是：", ele)
else:
    # 访问循环计数器的值，依然等于最后一个元素的值
    print("ele 块：", ele)

# 嵌套循环
for i in range(0, 5):
    j = 0
    while j < 3:
        print("i的值是%d,j的值是%d" % (i, j))
        j += 1

a_range = range(10)
a_list = [x * x for x in a_range]
print(a_list)

b_list = [x * x for x in a_range if x % 2 == 0]
print(b_list)


# 使用for表达式创建生成器
c_generator = [x * x for x in a_range if x % 2 == 0]
for i in c_generator:
    print(i, end='\t')


d_list = [(x, y) for x in range(5) for y in range(4)]
print(d_list)

src_a = [30, 12, 66, 34, 39, 78, 36, 51, 121]
src_b = [3, 5, 7, 11]
result = [(x, y) for x in src_b for y in src_a if y % x == 0]
print(result)










