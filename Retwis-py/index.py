import imp
import bottle
import settings
import session
import time
from convert import to_string, to_list, to_dict, to_set
from model import User, Post

r = settings.r


def islogin():
    sess = session.Session(bottle.request, bottle.response)
    if sess.is_new():
        return False
    else:
        return User(sess['id'])


@bottle.get('/')
@bottle.view('index')
def index():
    user = islogin()
    if user:
        res = {
            'username': user.username,
            'posts': user.posts(),
            'followers': user.followers(),
            'following': user.following(),
            'followers_num': user.followers_num(),
            'following_num': user.following_num()
        }
        return res
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

    user = User.create(username, password)

    if user:
        sess = session.Session(bottle.request, bottle.response)
        sess['id'] = user.id
        sess.save()

        bottle.redirect('/')

    return dict()


@bottle.post('/login')
@bottle.view('signup')
def login():
    username = bottle.request.POST['username']
    password = bottle.request.POST['password']
    user = User.find_by_username(username)
    if user:
        if user.password == password:
            sess = session.Session(bottle.request, bottle.response)
            sess['id'] = user.id
            sess.save()
            bottle.redirect('/')

    return dict()


# 退出
@bottle.get('/logout')
def logout():
    sess = session.Session(bottle.request, bottle.response)
    sess.invalid()
    bottle.redirect('/')


@bottle.post('/post')
def post():
    user = islogin()
    if user:
        content = bottle.request.POST['content']
        Post.create(user, content)
        bottle.redirect('/')

    else:
        bottle.redirect('/signup')


@bottle.get('/public/<filename:path>')
def send_static(filename):
    return bottle.static_file(filename, root='public/')


bottle.run(reloader=True)
