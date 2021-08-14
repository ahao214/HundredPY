# 二分查找

# li查找的数列
# val要查找的值


def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) / 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  # 带查找的值在mid的左侧
            right = mid - 1
        else:  # li[mid]<val 带查找的值在mid的右侧
            left = mid + 1
    else:
        return None
