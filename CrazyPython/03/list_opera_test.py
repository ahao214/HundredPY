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


