class URL(object):
    host = "https://www.zhihu.com"
    zhuanlan_host = "https://zhuanlan.zhihu.com"

    @classmethod
    def index(cls):
        # 首页
        return cls.host + ""
