# 重写父类的方法


class Bird:
    # Bird类的fly()方法
    def fly(self):
        print("我在天空飞翔...")


class Ostrich(Bird):
    # 重写Bird类的fly()方法
    def fly(self):
        print("我只能在地上跑...")


# 创建Ostrich对象
os = Ostrich()
os.fly()

print("-----------")


class BaseClass:
    def foo(self):
        print("父类中定义的foo方法")


class SubClass(BaseClass):
    # 重写父类的foo方法
    def foo(self):
        print("子类重写父类中的foo方法")

    def bar(self):
        print("执行bar方法")
        # 直接执行foo方法，将会调用子类重写之后的foo()方法
        self.foo()
        # 使用类名调用实例方法（未绑定方法）调用父类被重写的方法
        BaseClass.foo(self)


sc = SubClass()
sc.bar()

print("-----------")
print("使用super函数调用父类的构造方法")


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print('普通员工正在写代码，工资是：', self.salary)


class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address

    def info(self):
        print('我是一个顾客，我的爱好是：%s,地址是%s' % (self.favorite, self.address))


# Manager继承了Employee、Customer
# class Manager1(Employee, Customer):
#     pass


class Manager(Employee, Customer):
    # 重写父类的构造方法
    def __init__(self, salary, favorite, address):
        print('--Manager的构造方法--')

        # 通过super()函数调用父类的构造方法
        super().__init__(salary)
        # 使用未绑定方法调用父类的构造方法
        Customer.__init__(self, favorite, address)


# m = Manager1(25000)
# m.work()
# m.info()
print("-------")
m2 = Manager(20000, 'IT产品', '上海')
m2.work()
m2.info()

print("-----------")

print("-----------")
