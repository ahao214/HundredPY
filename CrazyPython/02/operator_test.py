import time

# 赋值运算符
s1 = "lph"
print(s1)

# 算术运算符
a = 5.2
b = 3.2
sum = a + b
print(sum)

# 对x求负
x = -0.5
x = -x
print(x)

e = 5.2
f = 3.1
print(e * f)

# * 可以作为字符串的连接运算符，表示将N个字符串连接起来
s3 = "crazy "
print(s3 * 5)


# / 表示普通除法
# // 表示整除，结果只有整数部分，小数部分被舍弃
aa = 5.2
bb = 3.1
print("aa/bb的值是：", aa/bb )
print("aa//bb的值是：", aa//bb)


# **:表示乘方运算符
print("5的2次方", 5**2)
print("2的3次方", 2**3)
print("4的开平方：", 4**0.5)
print("27开3次方：", 27 **(1/3))


# 索引运算符
print("索引运算符")

a = "abcdefghijklmn"
# 获取索引2到8，步长是3
print(a[2:8:3])

print(a[2:8])


a = time.gmtime()
b = time.gmtime()
# a和b相等，输出True
print(a == b)
# a和b不是同一个对象，输出False
print(a is b)


# 三目运算符
a = 5
b = 3
st = "a大于b" if a > b else "a不大于b"
print(st)


print("--in运算符--")
s = "crazyorg.it"
print('it' in s)
print('it' not in s)
print('cr' in s)




