# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline

class ZhihuPipeline(object):

    def __init__(self):
        # 初始化管道，用来处理item
        self.settings = get_project_settings()

    def process_item(self, item, spider):

        if item.__class__.__name__ == 'ZhihuQuestionItem':
            print(item)
        else:
            print(item)
