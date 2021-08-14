# 冒泡排序


def bubbleSort(li):
    for i in range(len(li) - 1):  # 第i趟
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
        print(li)


li = [2, 3, 9, 1, 8, 4, 6, 7, 0]
print(li)
bubbleSort(li)
