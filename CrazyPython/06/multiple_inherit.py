# 多继承


class Item:
    def info(self):
        print("Item中方法：", '这是一个商品')


class Product:
    def info(self):
        print("Product中方法：", '这是一个工业产品')


class Mouse(Item, Product):
    pass

class Keyboard(Product, Item):
    pass

m = Mouse()
m.info()

k = Keyboard()
k.info()

print("-----------")




