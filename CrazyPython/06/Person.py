# 类和对象
class Person:
    # 定义一个类变量
    hair = 'black'

    def __init__(self, name='Tom', age=8):
        # 下面为Person对象增加两个实例变量
        self.name = name
        self.age = age

    # 定义一个say方法
    def say(self, content):
        print(content)


p = Person()
print(p.name)
print(p.age)

p.say("人生苦短，我用Python")

print("重新赋值")
p.name = "Jerry"
print(p.name)

# 为p对象增加一个skills实例变量
p.skills = ["swimming","running"]
print(p.skills)

# 删除p对象的name实例变量
# del p.name
# print(p.name)


class InConstructor:
    def __init__(self):
        foo = 0
        self.foo = 6


print(InConstructor().foo)


print("-------------------")






