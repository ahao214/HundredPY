# while循环
import random

answer = random.randint(1, 10)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print("大一点")
    elif number > answer:
        print("小一点")
    else:
        print("恭喜你猜对了")
        break

print('你总共猜了%d次' % counter)
if counter > 3:
    print('你的智商余额明显不足')


