import re
import logging
from api.zhihu.utils import SignUrl


def login(session, headers, sign_info):
    # 请求login_url,udid_url,captcha_url加载所需要的cookie
    resp = session.get(SignUrl.api_signup(), headers=headers)
    logging.info("[INFO===>>>]请求{}，响应状态码:{}", SignUrl.api_signup(), resp.status_code)

    resp = session.post(SignUrl.api_udid(), headers=headers)
    logging.info("[INFO===>>>]请求{}，响应状态码:{}", SignUrl.api_udid(), resp.status_code)

    resp = session.get(SignUrl.api_captcha(), headers=headers)
    logging.info("[INFO===>>>]请求{}，响应状态码:{}", SignUrl.api_captcha(), resp.status_code)

    # 校验是否需要验证吗，需要则直接退出，还没遇到过需要验证码的
    if re.search('true', resp.text):
        logging.error('[ERROR===>>>]需要验证码')
        return session
        # exit()

    # post请求登陆接口
    resp = session.post(SignUrl.api_signin(), data=sign_info.encrypt_string, headers=headers)
    print("请求{}，响应状态码:{}".format(SignUrl.api_signin(), resp.status_code))

    # 校验是否登陆成功
    if re.search('user_id', resp.text):
        logging.info('[INFO===>>>]登陆成功')
    else:
        logging.error("[ERROR===>>>]登陆失败")
        # exit()
    return session
