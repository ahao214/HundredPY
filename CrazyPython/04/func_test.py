# 常用工具函数
# reversed - 反转
a = [23, 45, 56, 78, -90]
for x in reversed(a):
    print(x)

# sorted函数 - 排序
my_list = ["it", "vue", "js", "crazy"]
for s in sorted(my_list):
    print(s)

for i in range(0, 10):
    print("i的值是：", i)
    if i == 2:
        break;

for i in range(0, 10):
    print("i的值是：", i)
    if i == 2:
        break
    else:
        print("else块是：", i)

print("break")
exit_flag = False
for i in range(0, 5):
    for j in range(0, 3):
        print("i的值是%d,j的值是%d" % (i, j))
        if j == 1:
            exit_flag = True
            break
    if exit_flag:
        break

print("continue")
for i in range(0, 3):
    print("i的值是：", i)
    if i == 1:
        continue
    print("continue后的输出语句")

print("return")

def test():
    for i in range(10):
        for j in range(10):
            print("i的值是%d，j的值是%d" %(i, j))
            if j == 1:
                return
            print("return后面的语句")

test()

