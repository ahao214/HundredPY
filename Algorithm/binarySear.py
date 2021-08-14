# 二分查找

# li查找的数列
# val要查找的值


def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  # 带查找的值在mid的左侧
            right = mid - 1
        else:  # li[mid]<val 带查找的值在mid的右侧
            left = mid + 1
    else:
        return None


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(li, 4))
