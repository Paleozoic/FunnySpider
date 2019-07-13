import re


class URL(object):
    host = "https://www.zhihu.com"
    zhuanlan_host = "https://zhuanlan.zhihu.com"

    @staticmethod
    def find_url(string):
        # findall() 查找匹配正则表达式的字符串
        url = re.findall('src=\\"https://(.*?)\\"', string)
        return url

    @classmethod
    def index(cls):
        # 首页
        return cls.host + ""
