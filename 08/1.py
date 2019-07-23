class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_av(self):
        if self.age < 18:
            print('%s只能观看动画片.' % self.name)
        else:
            print('%s正在观看爱情片.' % self.name)

def main():
    stuone = Student('lph', 39)
    stuone.study('Python程序学习')
    stuone.watch_av()
    stutwo = Student('张帅', 17)
    stutwo.study('思想品德')
    stutwo.watch_av()

if __name__ == '__main__':
    main()