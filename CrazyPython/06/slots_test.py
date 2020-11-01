class Dog:
    __slots__ = ('walk', 'age','name')

    def __init__(self, name):
        self.name = name
    def test(self):
        print('预先定义的test方法')

d = Dog('Sonny')

from types import MethodType

d.walk = MethodType(lambda self:print('%s正在慢慢走' % self.name), d)

d.age = 5
d.walk()



