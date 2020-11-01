class Bird:
    def move(self, field):
        print('鸟在%s上自由的飞翔' % field)


class Dog:
    def move(self, filed):
        print('狗在%s上飞快的奔跑' % filed)


x = Bird()
x.move('天空')

x = Dog()
x.move('草地')


