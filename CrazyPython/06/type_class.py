def fn(self):
    print('fn函数')


# 使用type定义Dog类
# 第一个参数：创建的类名
# 第二个参数：该类继承的父类集合
# 第三个参数：该字典对象为该类绑定的类变量和方法
Dog = type('Dog', (object,), dict(walk=fn, age=6))

# 创建Dog对象
d = Dog()
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)
