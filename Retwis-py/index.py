import bottle
import settings
import session

r = settings.r


def islogin():
    sess = session.Session(bottle.request, bottle.response)
    if sess.is_new():
        return False
    else:
        return True


@bottle.get('/')
@bottle.view('index')
def index():
    if islogin():
        return dict()
    else:
        bottle.redirect('/signup')


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

        sess = session.Session(bottle.request, bottle.response)
        sess['id'] = uid
        sess.save()

        bottle.redirect('/')

    return dict()


@bottle.post('/login')
@bottle.view('signup')
def login():
    username = bottle.request.POST['username']
    password = bottle.request.POST['password']
    uid = r.hget('users', username).decode('utf-8')
    if uid:
        upassword = r.hget('user:{}'.format(uid), 'password').decode('utf-8')
        if password == upassword:
            sess = session.Session(bottle.request, bottle.response)
            sess['uid'] = uid
            sess.save()
            bottle.redirect('/')

    return dict()


@bottle.get('/public/<filename:path>')
def send_static(filename):
    return bottle.static_file(filename, root='public/')


bottle.run(reloader=True)
