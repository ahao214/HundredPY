# 顺序查找
# 时间复杂度O(n)


def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None
