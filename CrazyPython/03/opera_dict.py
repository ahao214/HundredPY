# clear 方法
cars = {"BMW": 90, "AUDI": 89}
print(cars)
cars.clear()
print(cars)

# get方法
cars = {"BMW": 90, "AUDI": 89}
print(cars.get('BMW'))
print(cars.get('LAB'))

# update方法
cars.update({"BMW": 900, "AUDI": 123})
print("使用update方法之后")
print(cars)

# items() key() value()
cars = {"BMW": 90, "AUDI": 89, "BENS": 78}
# key_value
ims = cars.items()
print(type(ims))
# 将dict_item转换为列表
print(list(ims))

# 打印出列表中的第二个
print(list(ims)[1])

# 所有的keys
kys = cars.keys()
print(type(kys))
print(list(kys))
print(list(kys)[1])

# 所有的values
vals = cars.values()
print(type(vals))
print(list(vals))
print(list(vals)[1])

# pop方法,用于获取指定key对应的value，并删除
print(cars)
cars.pop("AUDI")
print("使用pop之后")
print(cars)

# popitem 随机弹出字典中的一个key-value
cars = {"BMW": 90, "AUDI": 89, "BENS": 78}
print(cars.popitem())
print(cars)

k, v = cars.popitem()
print(k, v)

# setdefault方法
cars = {"BMW": 90, "AUDI": 89, "BENS": 78}

# 设置默认值，key不在cars中，新增key-value
print(cars.setdefault("ROP", 45))
print(cars)

# 设置默认值，key在cars中，不会修改cars的内容
print(cars.setdefault("BMW", 100))
print(cars)

# fromkeys方法
print("fromkeys方法")
a_dict = dict.fromkeys(['a', 'b'])
print(a_dict)

b_dict = dict.fromkeys((12, 13))
print(b_dict)

c_dict = dict.fromkeys((12, 13), 'good')
print(c_dict)

