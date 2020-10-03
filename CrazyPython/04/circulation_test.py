# 循环结构

# while循环
count_i = 0
while count_i < 10:
    print("count:", count_i)
    count_i += 1
print("循环结束")

print("循环遍历元祖中的数据")
a_tuple = ("apple", "banana", "orange")
i = 0
while i < len(a_tuple):
    print(a_tuple[i])
    i += 1

print("遍历循环list中的元素")
src_list = [12, 45, 34, 13, 100, 24, 56, 74, 109]
a_list = []
b_list = []
c_list = []
while len(src_list) > 0:
    # 弹出src_list最后一个元素
    ele = src_list.pop()
    if ele % 3 == 0:
        a_list.append(ele)
    if ele % 3 == 1:
        b_list.append(ele)
    else:
        c_list.append(ele)
print("整除3的：", a_list)
print("余数是1的：", b_list)
print("余数是2的：", c_list)

print("for循环语句")

s_max = input("请输入你想计算的阶乘：")
mx = int(s_max)
result = 1
for num in range(1, mx + 1):
    result *= num
print(result)

print("for遍历元祖")
a_tuple = ("C#", "VUE", "JS")
for ele in a_tuple:
    print("当前的元素是：", ele)

print("for遍历列表")
src_list = [12, 45, 3.4, 13, 'a', 4, 56,'it', 109.5]
my_sum = 0
my_count = 0
for ele in src_list:
    # 如果元素是整数或者浮点数
    if isinstance(ele, int) or isinstance(ele, float):
        print(ele)
        my_sum += ele
        my_count += 1
print("总数是：", my_sum)
print("平均数是：", my_sum / my_count)

a_list = [330, 4.5, 1.4, 'it', -3.5]
for i in range(0, len(a_list)):
    print("第%d个元素是%s" % (i, a_list[i]))


my_dict = {"语文": 90, "数学": 89, "英语": 98}
# 通过items方法返回key_value
for key, value in my_dict.items():
    print("key:", key)
    print("value:", value)

# 通过keys返回所有的key值
print("获取所有的key")
for key in my_dict.keys():
    print("key:", key)
    # 通过key值获取value
    print("value:", my_dict[key])

# 通过values()返回所有的value
print("获取所有的value")
for value in my_dict.values():
    print("value:", value)
print("-----")
src_list = [12, 45, 3.4, 12, 'it', 45, 3.4, 'it', 45, 3.4]
statistics = {}
for ele in src_list:
    # 如果字典statistics包含ele代表的key
    if ele in statistics:
        statistics[ele] += 1
    else:
        statistics[ele] = 1

# 遍历字典，打印ele出现的次数
for ele, count in statistics.items():
    print("%s 出现的次数为%d" %(ele, count))

