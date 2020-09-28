# 查找、替换
s = "crazyit.org is a good site"
# 判断s是否以crazyit开头
print(s.startswith("crazyit"))

# 判断s是否以site结尾
print(s.endswith("site"))

# 查询s中org出现的位置
print(s.find("org"))
print(s.index("org"))

# 从索引9处开始查找org出现的位置
print(s.find("org", 9))
print(s.index("org", 8)) # 引发错误

# 将字符串s中所有的it替换成XXXX
print(s.replace("it", "XXXX"))

# 将字符串s中1个it替换成XXXX
print(s.replace("it", "XXXX", 1))


# 定义翻译映射表
table = {97: 945, 98: 946, 116: 964}
print(s.translate(table))


