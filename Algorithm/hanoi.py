# 汉诺塔问题

# 移动n个圆盘
# 1、把n-1个圆盘从A柱子经过C柱子移动到B柱子
# 2、把第n个圆盘从A柱子移动到C柱子
# 3、把n-1个圆盘从B柱子经过A柱子移动到C柱子

# n表示圆盘的个数
# a b c 表示三个柱子
def hanoiAlgorithm(n, a, b, c):
    if n > 0:
        hanoiAlgorithm(n - 1, a, c, b)
        print("moving from %s to %s" % (a, c))
        hanoiAlgorithm(n - 1, b, a, c)


hanoiAlgorithm(3, "A", "B", "C")
