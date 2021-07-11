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
        # username = to_string(r.hget('user:{}'.format(uid), 'username'))
        # posts_id = to_list(r.lrange('user:{}:timeline'.format(uid), 0, 9))
        # posts = {}
        # # 博客
        # for pid in posts_id:
        #     post = to_dict(r.hgetall('post:{}'.format(pid)))
        #     post['username'] = to_string(
        #         r.hget('user:{}'.format(post['userid']), 'username'))
        #     posts[pid] = post

        # # 粉丝
        # followers = to_list(r.smembers('user:{}:followers'.format(uid)))
        # followers = [to_string(r.hget('user:{}'.format(uid), 'username'))
        #              for uid in followers]
        # # 粉丝数量
        # followers_num = r.scard('user:{}:followers'.format(uid))
        # # 关注
        # following = to_list(r.smembers('user:{}.following'.format(uid)))
        # following = [to_string(r.hget('user:{}'.format(uid), 'username'))
        #              for uid in following]
        # # 关注数量
        # following_num = r.scard('user:{}:following'.format(uid))

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

    user=User.create(username,password)

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
    user=User.find_by_username(username)
    if user:        
        if user.password == password:
            sess = session.Session(bottle.request, bottle.response)
            sess['id'] = user.id
            sess.save()
            bottle.redirect('/')

    return dict()


@bottle.post('/post')
def post():
    user = islogin()
    if user:
        content = bottle.request.POST['content']
        Post.create(user,content)
        bottle.redirect('/')

    else:
        bottle.redirect('/signup')


@bottle.get('/public/<filename:path>')
def send_static(filename):
    return bottle.static_file(filename, root='public/')


bottle.run(reloader=True)
