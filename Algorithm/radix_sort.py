# 基数排序
import random


def radixSort(li):
    maxNum = max(li)  # li中的最大值
    it = 0
    while 10 ** it <= maxNum:
        buckets = [[] for _ in range(10)]  # 创建10个桶，编号从0到9
        for values in li:
            digit = (values // 10 ** it) % 10  # 获取数字的最后一位的数字
            buckets[digit].append(values)  # 把数字放到对应的桶里面
        li.clear()

        for buc in buckets:
            li.extend(buc)
        it += 1


li = list(range(1000))
random.shuffle(li)
print(li)
radixSort(li)
print("执行基数排序方法之后：")
print(li)
