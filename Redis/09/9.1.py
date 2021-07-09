import redis

# 使用redis记录用户在线状态

client = redis.Redis(host='127.0.0.1')


def set_online_status(user_id):
    """
    当用户登录网站时，调用这个函数在Redis中设置一个字符串
    :param user_id: 用户账号
    :return: None
    """
    client.set(user_id, 1)


def set_offline_status(user_id):
    """
    当用户退出网站时调用这个函数，从Redis中删除这个以用户账号为Key的字符串
    :param user_id: 用户账号
    :return: None
    """
    client.delete(user_id)


def check_online_status(user_id):
    """
    检查用户是否在线，如果在线，则得到用户账号对应的Key就会返回1，否则返回None
    :param user_id: 用户账号
    :return: bool
    """
    online_status = client.get(user_id)
    if online_status and online_status.decode() == '1':
        return True
    return False
