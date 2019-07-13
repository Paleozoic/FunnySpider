import os


class Conf(object):
    # ZHIHU_JS_PATH = 'api/zhihu/html/zhihu.js'
    CONF_PATH = os.path.dirname(os.path.abspath(__file__))
    ZHIHU_JS_PATH = os.path.join(CONF_PATH, '..', 'html', 'zhihu.js')
