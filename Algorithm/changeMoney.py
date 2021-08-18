# 零钱找零

t = [100, 50, 20, 5, 1]


def change(t, n):
    """

    :param t: 表示钱币的面额
    :param n: 表示零钱的总数
    :return:
    """
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n


print(change(t, 376))
