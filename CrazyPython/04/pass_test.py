# pass语句
s = input("请输入一个整数:")
s = int(s)
if s > 5:
    print("大于5")
elif s < 5:
    pass
else:
    print("等于5")