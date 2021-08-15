# 插入排序


def insertSort(li):
    for i in range(1, len(li)): # i表示摸到的牌的下标
        tmp = li[i]
        j = i - 1       # j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        print(li)


li = [23, 4, 9, 8, 1, 5, 7, 12]
insertSort(li)
print(li)
