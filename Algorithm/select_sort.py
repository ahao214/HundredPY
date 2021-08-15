# 选择排序


# 简单的选择排序
def selectSortSample(li):
    # 创建一个新的列表
    new_li = []
    for i in range(len(li)):
        min_val = min(li)
        new_li.append(min_val)
        li.remove(min_val)
    return new_li


def selectSort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)


li = [2, 3, 4, 9, 8, 7, 5, 1]
# print(selectSortSample(li))
selectSort(li)
print(li)
