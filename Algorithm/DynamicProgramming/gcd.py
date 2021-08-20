# 最大公约数

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


print(gcd(12, 16))


def gcd2(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


print(gcd2(12, 16))
