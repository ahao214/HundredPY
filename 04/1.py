sum = 0
for x in range(101):
    sum += x
print(sum)

# 利用for循环实现1-100之间的偶数求和
count = 0
for x in range(2,101,2):
    count += x
print(count)

sumone = 0
for x in range(1, 101):
    if x % 2 == 0:
        sumone += x
print(sumone)