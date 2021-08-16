# 归并排序

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:  # 只要左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while执行完，肯定有一部分没有数字
    while i <= mid:
        ltmp.append(li[i])
        i += 1

    while j <= high:
        ltmp.append(li[j])
        j += 1

    li[low:high + 1] = ltmp


def mergeSort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(li, low, mid)
        mergeSort(li, mid + 1, high)
        merge(li, low, mid, high)


# li = [2, 4, 8, 9, 1, 3, 5]
# merge(li, 0, 3, 6)
# print(li)


li = [23, 4, 9, 8, 1, 5, 7, 12]
mergeSort(li, 0, len(li)-1)
print(li)
