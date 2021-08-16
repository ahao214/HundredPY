# 计数排序

def countSort(li, maxCount=100):
    count = [0 for _ in range(maxCount + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)


li = [1, 1, 3, 4, 5, 6, 1, 4, 5, 2, 3, 6]
print(li)
countSort(li)
print(li)
