import os
print(os.path.abspath('.'))
print(os.path.abspath('..'))
# 判断路径是否存在
print(os.path.exists('F:/MyProgramm/python/hundred'))
# 判断是否是文件
print(os.path.isfile('F:/MyProgramm/python/hundred'))
# 判断是否是路径
print(os.path.isdir('F:/MyProgramm/python'))
