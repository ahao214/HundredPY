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



