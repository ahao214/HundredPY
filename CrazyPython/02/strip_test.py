# 删除空白

s1 = " i think it is good "
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())


print("-------")
s2 = "i think it is a scarecrow"
# 删除左边的i t o w 字符
print(s2.lstrip('itow'))
# 删除右边的i t o w 字符
print(s2.rstrip('itow'))
# 删除两边的i t o w 字符
print(s2.strip('itow'))
