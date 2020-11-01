def fn(self):
    print('fn函数')


# 使用type定义Dog类
Dog = type('Dog', (object,), dict(walk=fn, age = 6))

# 创建Dog对象
d = Dog()
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)