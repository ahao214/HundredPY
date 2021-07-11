def info(code, msg):
    res = {
        'code': code,
        'msg': msg
    }
    return res


def succ(msg):
    return info(200, msg)


def fail(msg):
    return info(-1, msg)
