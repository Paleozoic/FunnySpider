from api.zhihu.Zhihu import Zhihu


# 登录访问
def login_zhihu(username, password):
    zhihu = Zhihu(username, password)
    zhihu.login()
    return zhihu


# 匿名访问
def anon_zhihu():
    zhihu = Zhihu()
    return zhihu
