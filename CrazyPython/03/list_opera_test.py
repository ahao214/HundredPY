# 列表的操作

print("增加列表元素")
a_list = ["c", 20, -10]
a_list.append("aho")
print(a_list)

a_tuple =("1", "b")
# 将元祖追加到列表中
a_list.append(a_tuple)
print(a_list)

# 追加列表
a_list.append(['a','c'])
print(a_list)

print("extend方法")
b_list = ["a", "b"]
# 追加的列表不能当成一个整体,使用extend方法
b_list.extend((2, 3))
print(b_list)

b_list.extend(["c","d"])
print(b_list)

b_list.extend(range(1,10, 2))
print(b_list)

print("insert()方法")
c_list = list(range(1,10,2))
print(c_list)

# 在索引3处插入字符串
c_list.insert(3, "d")
print(c_list)



print("删除列表元素")
a_list =["crazy", 20, -10, ("a", "b"), "ahao"]
# 删除第3个元素
del a_list[2]
print(a_list)
# 删除第2个到第4个元素
del a_list[1:3]
print(a_list)

b_list = list(range(1,10))
print(b_list)
# 删除第3个到倒数第2个元素，间隔是2
del b_list[2:-2:2]
print(b_list)
# 删除第3个到第5个元素，间隔是2
del b_list[2:4:2]
print(b_list)


print("remove方法")
c_list =["crazy", 20, -10, ("a", "b"), "ahao"]
print(c_list)
c_list.remove(20)
print(c_list)

print("clear方法")
c_list.clear()
print(c_list)

