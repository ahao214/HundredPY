# 控制台五子棋

# 定义棋盘大小
BOARD_SIEZ = 15

# 定义一个二维列表来充当棋盘
board = []


def initBoard():
    # 为每个元素赋值“+”，用于在控制台画出棋盘
    for i in range(BOARD_SIEZ):
        row = ["+"] * BOARD_SIEZ
        board.append(row)


# 在控制台输出棋盘的方法
def printBoard():
    # 打印每个列表元素
    for i in range(BOARD_SIEZ):
        for j in range(BOARD_SIEZ):
            # 打印列表元素后不换行
            print(board[i][j], end="")
        # 每打印完一行列表元素后输出一个换行符
        print()


initBoard()
printBoard()
inputStr = input("请输入您下棋的坐标，应以x,y的格式:\n")


while inputStr is not None:
    # 将用户输入的字符串以逗号(,)作为分隔符，分割成两个字符串
    x_str, y_str = inputStr.split(sep=",")
    # 为对应的列表元素赋值"*"
    board[int(y_str) - 1][int(x_str) - 1] = "*"
    '''
    电脑随机生成两个整数，作为电脑下棋的坐标，赋值给board列表
    还涉及
        1、坐标的有效性，只能是数字，不能超出棋盘范围
        2、下的棋的点，不能重复下棋
        3、每次下棋后，需要扫描谁赢了		
    '''
    printBoard()
    inputStr = input("请输入您下棋的坐标，应以x,y的格式：\n")









