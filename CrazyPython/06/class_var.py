# 成员变量

class Address:
    detail = '广州'
    post_code = '510660'

    def info(self):
        # 尝试直接访问类变量
        # print(detail) # 报错
        # 通过类来访问变量
        print(Address.detail)
        print(Address.post_code)


# 通过类来访问Address类的类变量
print(Address.detail)
addr = Address()
addr.info()
# 修改Address类的类变量
Address.detail = '佛山'
Address.post_code = '457890'
addr.info()

print("----------------")


class Record:
    # 定义两个类变量
    item = '鼠标'
    date = '2020-09-09'

    def info(self):
        print('info方法中：', self.item)
        print('info方法中：', self.date)


rc = Record()
print(rc.item)
print(rc.date)
rc.info()

print('修改Record两个类变量之后')
# 修改Record两个类变量
rc.item = '键盘'
rc.date = '2020-09-10'
rc.info()

print('--------')


class Inventory:
    # 定义两个类变量
    item = '鼠标'
    quantity = 2000

    # 定义实例方法
    def change(self, item, quantity):
        # 下面赋值语句不是对类变量赋值，而是定义新的实例变量
        self.item = item
        self.quantity = quantity


# 创建Inventory对象
iv = Inventory()
iv.change('显示器', 5000)
# 访问iv的item和quantity实例变量
print(iv.item)
print(iv.quantity)
# 访问Inventory的item和quantity类变量
print(Inventory.item)
print(Inventory.quantity)

print('--------')


