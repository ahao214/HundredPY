# 使用字典格式化字符串

# 在字符串模板中使用key
temp = '书名是：%(name) s,价格是：%(price) 010.2f,出版社是：%(publish)s'
book = {'name': '疯狂的讲义', 'price': 88.8, 'publish': '电子设'}

# 使用字典为字符串模板中的key传入值
print(temp % book)

book = {'name':'风景好','price':90, 'publish':'清华出版社'}

# 使用字典为字符串模板中的key传入值
print(temp % book)






