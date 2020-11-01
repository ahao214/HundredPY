class Canvas:
    def draw_pit(self, shape):
        print('--开始绘图--')
        shape.draw(self)


# 长方形
class Rectangle:
    def draw(self, canvas):
        print('在%s上绘制矩形' % canvas)


class Triangle:
    def draw(self, canvas):
        print('在%s上绘制三角形' % canvas)


class Circle:
    def draw(self, canvas):
        print('在%s上绘制圆形' % canvas)


c = Canvas()
c.draw_pit(Rectangle())
c.draw_pit(Triangle())
c.draw_pit(Circle())

