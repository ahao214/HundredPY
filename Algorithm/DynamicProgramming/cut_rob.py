# 钢条切割问题

import time


def calTime(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time:%s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper()


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


# 自顶向下实现
def cut_rob_recurision_1(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rob_recurision_1(p, i) + cut_rob_recurision_1(p, n - i))
        return res


# 自顶向下实现
def cut_rob_recurision_2(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rob_recurision_2(p, n - i))
        return res


print(cut_rob_recurision_1(p, 9))
print(cut_rob_recurision_2(p, 9))


# 自底向上实现
def cut_rob_db(p, n):
    r = [0]
    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i - j])
        r.append(res)
    return r[n]


print(cut_rob_db(p, 9))


def cut_rob_extend(p, n):
    r = [0]
    s = [0]
    for i in range(1, n + 1):
        res_r = 0  # 价格的最大值
        res_s = 0  # 价格最大值对应方案的左边不切割部分的长度
        for j in range(1, i + 1):
            if p[j] + r[i - j] > res_r:
                res_r = p[j] + r[i - j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s


print(cut_rob_extend(p, 9))


def cut_rob_solution(p, n):
    r, s = cut_rob_extend(p, n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans


print(cut_rob_solution(p, 7))
