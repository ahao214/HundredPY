scores = {"语文" : 89}
print(scores)
# 通过key访问
print(scores["语文"])

scores["数学"] = 80
scores[23] = 98
print(scores)


# 使用del删除
del scores[23]
del scores["语文"]
print(scores)

cars = {"BMW": 8.5, "BENS": 8.3, "AUDI": 7.7}
print(cars)

# in 和not in
print('BMW' in cars)
print('lab' in cars)
print('aa' not in cars)



