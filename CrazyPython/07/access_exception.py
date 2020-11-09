def foo():
    try:
        fis = open("a.txt")
    except Exception as e:
        print(e.args)

foo()
