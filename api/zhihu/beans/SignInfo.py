import time
import hmac
from hashlib import sha1
import execjs
from api.zhihu.conf.Conf import Conf


class SignInfo(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.time_str = str(int(time.time() * 1000))
        self.signature = SignInfo.get_signature(self.time_str)
        self.encrypt_string = SignInfo.encrypt(self.append_string())

    @staticmethod
    def get_signature(now):
        h = hmac.new(key='d1b964811afb40118a12068ff74a12f4'.encode('utf-8'), digestmod=sha1)
        grant_type = 'password'
        client_id = 'c3cef7c66a1843f8b3a9e6a1e3160e20'
        source = 'com.api.web'
        h.update((grant_type + client_id + source + now).encode('utf-8'))
        return h.hexdigest()

    @staticmethod
    def encrypt(string):
        with open(Conf.ZHIHU_JS_PATH, 'r', encoding='utf-8') as f:
            js = f.read()
        result = execjs.compile(js).call('encrypt', string)
        return result

    def append_string(self):
        # 拼接需要加密的字符串
        string = "client_id=c3cef7c66a1843f8b3a9e6a1e3160e20&grant_type=password&timestamp={}&source=com.api.web&signature={}&username={}&password={}&captcha=&lang=en&ref_source=homepage&utm_source=".format(
            self.time_str, self.signature, self.username, self.password)
        return string
