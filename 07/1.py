# 在屏幕上显示跑马灯效果

import os
import time
def main():
    content = "我喜欢篮球，喜欢看NBA"
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear)
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:]

if __name__ =='__main__':
    main()










