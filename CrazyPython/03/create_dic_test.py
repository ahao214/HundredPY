# 创建字典
scores = {"语文": 89, "数学": 90, "英语": 90}
print(scores)

emp_dic = {}

# 元祖作为dic的key
dic2 = {(20, 30): "good", 30:"bad"}
print(dic2)

colors = [('red', 10), ('black', 20), ('yellow', 30)]
dic_color = dict(colors)
print(dic_color)

cars = [['bmw', 1500], ['byd', 1300], ['hhh', 10]]
print(dict(cars))

# 使用关键字参数来创建字典
dictsix = dict(spinach = 1.39, cabbage = 1.29 )
print(dictsix)
