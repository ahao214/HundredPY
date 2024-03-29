# 拼接最大数

from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]


def xy_cmp(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


def numberdJoin(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp))
    return "".join(li)


print(numberdJoin(li))