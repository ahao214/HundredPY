# 读写JSON文件

import json
def main():
    mydict = {
        "name":"lph",
        "age":24,
        "qq":123456,
        "wechar":"lph99",
        "friends":["拿破仑","彼得大帝"],
        "cars":[
             {"brand":"BYD","max_speed":80},
            {"brand":"Audi","max_speed":180},
            {"brand":"Benz","max_speed":280}
        ]
    }

    try:
        with open('one.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成')

if __name__ == '__main__':
    main()