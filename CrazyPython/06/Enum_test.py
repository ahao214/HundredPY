import enum


# 定义season枚举类
class Season(enum.Enum):
    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4


print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)

print(Season['SUMMER'])

print(Season(3))

# 遍历枚举
for name, member in Season.__members__.items():
    print(name, '=>', member, ',', member.value)
