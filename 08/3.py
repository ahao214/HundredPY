# 定义一个类描述数字时钟
class Clock(object):
    """数字时钟"""
    def __init__(self, hour = 0, minute = 0, second = 0):
        """
        初始化方法
        :param hour:
        :param minute:
        :param second:
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 1
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute,self._second)
def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())

        clock.run()

if __name__ == '__main__':
    main()






