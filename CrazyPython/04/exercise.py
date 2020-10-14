# 小例子：绕圈圈

SIZE = 7
array = [[0] * SIZE]
# 创建衣蛾长度是SIZE * SIZE的二维列表
for i in range(SIZE - 1):
    array += [[0] * SIZE]

# 该orient代表绕圈的方向
# 其中0表示向下、1表示向右、2表示向左、3表示向上
orient = 0
# 控制将1~SIZE * SIZE的数值填入二维列表中
# 其中i控制行索引，k控制列索引
j = 0
k = 0
for i in range(1, SIZE * SIZE + 1):
    array[j][k] = i

    if j + k == SIZE - 1:
        # j>k,位于左下角
        if j > k:
            orient = 1
        # 位于右上角
        else:
            orient = 2
    elif (k == j) and (k >= SIZE / 2):
        orient = 3
    elif (j == k - 1) and (k <= SIZE / 2):
        orient = 0

    # 根据方向来控制行索引、列索引的改变
    # 如果方向为向下绕圈：
    if orient == 0:
        j += 1
    # 如果方向为向右绕圈：
    elif orient == 1:
        k += 1
    # 如果方向为向左绕圈：
    elif orient == 2:
        k -= 1
    # 如果方向为向上绕圈：
    elif orient == 3:
        j -= 1

# 采用变量输出上面二维列表
for i in range(SIZE):
    for j in range(SIZE):
        print('%02d' % array[i][j], end=" ")
    print("")











