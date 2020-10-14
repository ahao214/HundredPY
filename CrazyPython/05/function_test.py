# 函数


# 定义一个函数，声明两个形参
def max_value(x, y):
    z = x if x >y else y
    return z


def say_name(name):
    print("正在执行say_name函数")
    return name + "，你好"


a = 9
b = 3
result = max_value(a, b)
print(result)

print(say_name("孙悟空"))

print("-------")



# 返回多个值
def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        # 如果元素e是数值
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum / count


my_list = [20, 15, 30, 'a', 35]
# 获取sum_and_avg函数返回的多个值，多个返回值被封装成元祖
tp = sum_and_avg(my_list)
print(tp)





