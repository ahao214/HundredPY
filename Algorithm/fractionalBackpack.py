# 分数背包

goods = [(60, 10), (120, 30), (100, 20)]  # 每个商品元组表示(价格、重量)

# 按照每千克的价格倒序排序
goods.sort(key=lambda x: x[0] / x[1], reverse=True)


def backpack(goods, w):
    """

    :param goods:
    :param w: 背包的重量
    :return:
    """
    m = [0 for _ in range(len(goods))]
    totalV = 0
    for i, (price, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            totalV += price
            w -= weight
        else:
            m[i] = w / weight
            totalV += m[i] * price
            w = 0
            break
    return totalV, m


print(backpack(goods, 50))