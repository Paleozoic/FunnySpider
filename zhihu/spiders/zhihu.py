import scrapy
from scrapy.utils.project import get_project_settings

from zhihu.spiders.login import login
from api.zhihu import Zhihu


class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    start_urls = ['https://zhihu.com']
    allowed_domains = ['www.zhihu.com']
    # settings.py的属性
    setting = get_project_settings()

    zhihu: Zhihu = login.anon_zhihu()

    offset = 0
    limit = 20

    # def start_requests(self):
    #     yield scrapy.Request('https://www.zhihu.com/', callback=self.parse)

    def parse(self, response):
        answers = self.zhihu.get_answers(question_id=1, offset=self.offset, limit=self.limit)
        if answers:
            self.offset = self.offset + self.limit
            yield scrapy.Request('https://www.zhihu.com/', callback=self.parse)
            for answer in answers['data']:
                print(answer['author']['name'])
