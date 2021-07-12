import redis
import bottle
from response import info, succ, fail

r = redis.StrictRedis()

# 访问频率限流

# 装饰器


def limit_rate(func):
    def api(*args, **kwagrs):
        ip = bottle.request.remote_addr
        name = func.__name__
        key = 'limit:rate:{}:{}'.format(ip, name)
        if r.exists(key):
            rate = r.incr(key)
            if rate > 5:
                return fail('IP:{},访问频率过高'.format(ip))
            return succ('IP{},访问次数：{}'.format(ip, rate))

        pipe = r.pipeline()
        pipe.incr(key)
        pipe.expire(key, 60)
        pipe.execute()
        return succ('IP:{},访问次数：{}'.format(ip, 1))
    return api


@bottle.get('/api')
@limit_rate
def api():
    return succ('正常接口')


@bottle.get('/')
def index():
    bottle.redirect('/api')


bottle.run(reloader=True)
