# topk问题

import random


# 建立小根堆


def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
        li[i] = tmp


def topk(li, k):
    heap = li[0:k]
    # 建堆
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)
    # 遍历
    for i in range(k, len(li) - 1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)

    # 输出
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)

    return heap


li = list(range(1000))
random.shuffle(li)

print(topk(li, 10))
