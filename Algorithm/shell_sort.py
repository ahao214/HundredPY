# 希尔排序

def shell(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


def shellSort(li):
    d = len(li) // 2
    while d >= 1:
        shell(li, d)
        d //= 2


li = [2, 3, 4, 1, 5, 9, 0, 8, 7]
shellSort(li)
print(li)
