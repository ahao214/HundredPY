import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
    print("你输入的两个数相除的结果是：", c)



except (ValueError, ArithmeticError, IndexError):
    print("数值错误：程序只能接受整数参数;索引错误：运行程序时输入的参数个数不对")


except Exception:
    print("未知异常")
