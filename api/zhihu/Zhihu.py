import requests
import json
from api.zhihu.opt import SignOpt, QuesOpt
from api.zhihu.beans.SignInfo import SignInfo
from api.zhihu.utils.AnsUrl import AnsUrl


class Zhihu(object):

    def __init__(self, username=None, password=None):
        self.time_str = 0
        self.sign_info = SignInfo(username, password)
        self.session = requests.session()
        # 此处请求头只需要这三个
        self.headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'x-zse-83': '3_1.1'
        }

    def login(self):
        self.session = SignOpt.login(session=self.session, headers=self.headers, sign_info=self.sign_info)

    def get_answers(self, question_id, offset, limit):
        ans_url = AnsUrl.answers(question_id, offset, limit)
        resp = self.session.get(ans_url, headers=self.headers)
        # 转化json
        answers = json.loads(resp.text)
        return answers

    def download_imgs(self, question_id, offset, limit, img_path):
        QuesOpt.download_imgs(self, question_id=question_id, offset=offset, limit=limit, img_path=img_path)

    def download_all_imgs(self, question_id, img_path):
        offset = 0
        limit = 20
        paging = {
            'is_end': False
        }
        while not paging['is_end']:
            paging = QuesOpt.download_imgs(self, question_id=question_id, offset=offset, limit=limit, img_path=img_path)
            # &offset=15
            offset = offset + limit
