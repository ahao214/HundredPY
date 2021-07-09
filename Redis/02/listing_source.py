import time


# 尝试获取并返回令牌对应的用户
def check_token(conn, token):
    return conn.hget('login:', token)


# 更新令牌的方法
def update_token(conn, token, user, item=None):
    timestamp = time.time()  # 获取当前时间戳
    conn.hset('login:', token, user)  # 维持令牌与已登录用户之间的映射
    conn.zadd('recent:', token, timestamp)  # 记录令牌最后一次出现的时间
    if item:
        conn.zadd('viewed:' + token, item, timestamp)  # 记录用户浏览过的商品
        conn.zremrangebyrank('viewed:' + token, 0, -26)  # 最近浏览过的25个商品


# 清理旧会话
QUIT = False
LIMIT = 10000000


def clean_sessions(conn):
    while not QUIT:
        size = conn.zcard('recent:')  # 找出目前已有令牌的数量
        if size <= LIMIT:  # 如果令牌数未超过限制，休眠并在之后重新检查
            time.sleep(1)
            continue
        # 获取需要移除的令牌ID
        end_index = min(size - LIMIT, 100)
        tokens = conn.zrange('recent:', 0, end_index)
        # 为那些将要被删除的令牌构建键名
        session_key = []
        for token in tokens:
            session_key.append('viewed:' + token)
        # 移除最旧的那些令牌
        conn.delete(*session_key)
        conn.hdel('login:', *token)
        conn.zrem('recent:', *token)


# 更细购物车
def add_to_cart(conn, session, item, count):
    if count <= 0:
        conn.hrem('cart:' + session, item)  # 从购物车中移除指定的商品
    else:
        conn.hset('cart:' + session, item, count)  # 将指定的商品添加到购物车


def clean_full_sessions(conn):
    while not QUIT:
        size = conn.zcard('recent:')
        if size <= LIMIT:
            time.sleep(1)
            continue

        end_index = min(size - LIMIT, 100)
        sessions = conn.zrange('recent:', 0, end_index - 1)

        session_keys = []
        for sess in sessions:
            session_keys.append('viewed:' + sess)
            session_keys.append('cart:' + sess)

        conn.delete(*session_keys)
        conn.hdel('login:', *sessions)
        conn.zrem('recent:', *sessions)
