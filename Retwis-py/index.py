import bottle
import settings

r = settings.r


@bottle.get('/')
@bottle.view('index')
def index():
    return dict()


@bottle.get('/signup')
@bottle.view('signup')
def signup():
    return dict()


@bottle.post('/signup')
@bottle.view('signup')
def signup():
    username = bottle.request.POST['username']
    password = bottle.request.POST['password']

    # 判断uid是否已经注册
    uid = r.hget('users', username)
    if not uid:
        uid = r.incr('user:id')
        udata = {
            'username': username,
            'password': password
        }
        r.hmset('user:{}'.format(uid), udata)
        r.hset('users', username, uid)
        bottle.redirect('/')
        
    return dict()

bottle.run(reloader=True)
