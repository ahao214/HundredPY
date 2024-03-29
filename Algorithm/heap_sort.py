# 堆排序


def sift(li, low, high):
    """

    :param li:列表
    :param low:堆的根结点位置
    :param high:堆的最后一个元素的位置
    :return:
    """
    i = low  # i最开始指向根结点
    j = 2 * i + 1  # 左节点
    tmp = li[low]  # 把堆顶存起来
    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:  # 右节点大于左节点
            j = j + 1  # j指向右节点
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:
            li[i] = tmp  # 把tmp放到某一级的位置上
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上


def heapSort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        # i表示建堆的时候调整的部分的根的下标
        sift(li, i, n - 1)

    for i in range(n - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i-1是新的high


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
heapSort(li)
print(li)
