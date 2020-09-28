# 分割、连接方法

s = "crazyit.org is a good site"
print(s.split())

# 使用空白对字符串分割，最多只分割前两个字符
print(s.split(None, 2))

# 使用.分割
print(s.split("."))

mylist = s.split()

# 使用'/'作为分隔符，将mylist连接为字符串
print('/'.join(mylist))





