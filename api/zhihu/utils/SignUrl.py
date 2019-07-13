import time
from api.zhihu.utils.URL import URL


class SignUrl(URL):

    @classmethod
    def api_signup(cls):
        # API signup
        return cls.host + "/signup?next=/"

    @classmethod
    def api_udid(cls):
        # API udid
        return cls.host + "/udid"

    @classmethod
    def api_signin(cls):
        # API登陆
        return cls.host + "/api/v3/oauth/sign_in"

    @classmethod
    def api_captcha(cls):
        return cls.host + "/api/v3/oauth/captcha?lang=en"

    @classmethod
    def email_login(cls):
        # 邮箱登录
        return cls.host + "/login/email"

    @classmethod
    def phone_login(cls):
        # 手机登录
        return cls.host + "/login/phone_num"

    @classmethod
    def captcha(cls, _type="login"):
        # 验证码
        return cls.host + "/captcha.gif?r={timestamp}&type={type}".format(timestamp=str(int(time.time() * 1000)),
                                                                          type=_type)

    @classmethod
    def register_sms_code(cls):
        # 注册用的短信验证码
        return cls.host + "/send_register_verification_code/sms"

    @classmethod
    def register_validate(cls):
        # 注册验证URL
        return cls.host + "/register/phone_num/validation"

    @classmethod
    def register(cls):
        return cls.host + "/register/phone_num"
