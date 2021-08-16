# 桶排序
import random


def bucketSort(li, n=100, maxNum=10000):
    """

    :param li: 列表
    :param n: 桶的数量
    :param maxNum: 数字的数量
    :return:
    """
    buckets = [[] for _ in range(n)]  # 创建桶
    for var in li:
        i = min(var // (maxNum // n), n - 1)  # i表示var放在几号桶里面
        buckets[i].append(var)  # 把var加到桶里面
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li


li = [random.randint(0, 10000) for i in range(10000)]
print(li)
li = bucketSort(li)
print(li)
