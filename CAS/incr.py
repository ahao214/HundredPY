import redis
r = redis.StrictRedis()


def incr(key):
    r.watch(key)
    val = r.get(key)
    if not val:
        val = 0
    val = int(val)+1
    pipe = r.pipeline()
    pipe.set(key, val)
    pipe.execute()


incr('foo')
print(r.get)
