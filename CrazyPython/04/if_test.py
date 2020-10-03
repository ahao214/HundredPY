# if
s_age = input("请输入你的年龄：")
age = int(s_age)
my_age = int(s_age)
if age > 20:
    print("你已经20岁了")

if my_age > 60:
    print("老年人")
elif my_age > 40:
    print("中年人")
elif my_age > 20:
    print("青年人")

print("-------------")
s = ""
if s :
    print("s不是空字符")
else:
    print("s是空字符")

my_list = []
if my_list:
    print("my_list不是空列表")
else:
    print("my_list是空列表")

my_dict = {}
if my_dict:
    print("my_dict不是空字典")
else:
    print("my_dict是空字典")