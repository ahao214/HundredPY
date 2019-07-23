class Test:
    def __init__(self, foo):
        self.foo = foo

    def bar(self):
        print(self.foo)
        print('bar')

def main():
    test = Test('hello')
    test.bar()
    print(test.foo)

if __name__ == '__main__':
    main()