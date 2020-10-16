# 继承

class Fruit:
    def info(self):
        print("我是一个水果！重%g克" % self.weight)


class Food:
    def taste(self):
        print("不同食物的口感不同")


# 定义Apple类，继承了Fruit类和Food类
class Apple(Fruit, Food):
    pass


# 创建Apple对象
a = Apple()
a.weight = 5.6

# 调用Apple对象的info()方法
a.info()
# 调用Apple对象的taste()方法
a.taste()
