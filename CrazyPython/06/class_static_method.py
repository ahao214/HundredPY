# 类方法和静态方法


class Bird:
    # 使用@classmethod修饰的方法是类方法
    @classmethod
    def fly(cls):
        print('类方法fly：', cls)

    # 使用@staticmethod修饰的方法是静态方法
    def info(p):
        print('静态方法info：', p)


# 调用类方法，Bird类会自动绑定到第一个参数
Bird.fly()

Bird.info("crazyit")

# 创建Bird对象
b = Bird()
b.fly()

