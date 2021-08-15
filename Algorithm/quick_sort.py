# 快速排序


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找比tmp小的值
            right -= 1
        li[left] = li[right]
        # print(li)
        while left < right and li[left] <= tmp:  # 从左边找比tmp大的值
            left += 1
        li[right] = li[left]
        # print(li)
    li[left] = tmp
    return left


def quickSort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quickSort(li, left, mid - 1)
        quickSort(li, mid + 1, right)


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
# print(li)
# partition(li, 0, len(li) - 1)
# print(li)
quickSort(li, 0, len(li)-1)
print(li)

