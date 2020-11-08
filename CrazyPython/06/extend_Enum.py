import enum


class Orientation(enum.Enum):
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'

    def info(self):
        print('这是一个代表方向【%s】的枚举' % self.value)


print(Orientation.SOUTH)
print(Orientation.SOUTH.value)
# 通过枚举变量名访问枚举
print(Orientation['WEST'])
# 通过枚举值访问枚举
print(Orientation('南'))

# 调用枚举的info()方法
Orientation.EAST.info()

# 遍历枚举
for name, member in Orientation.__members__.items():
    print(name, '=>', member, ',', member.value)



