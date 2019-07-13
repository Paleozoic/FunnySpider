import re
import json
import scrapy
from scrapy.utils.project import get_project_settings

setting = get_project_settings()
headers = setting['DEFAULT_REQUEST_HEADERS']
answer_count = setting['ANSWER_COUNT_PER_QUESTION']
answer_offset = setting['ANSWER_OFFSET']

# 点击查看更多答案触发的url
more_answer_url = 'https://www.zhihu.com/api/v4/questions/{0}/answers?include=data%5B*%5D.i' \
                  's_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_actio' \
                  'n%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_ed' \
                  'it%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2' \
                  'Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Crevie' \
                  'w_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2' \
                  'Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.ur' \
                  'l%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.t' \
                  'opics&offset={1}&limit={2}&sort_by=default'


def parse_question(self, response):
    """ 解析问题详情及获取指定范围答案 """
    text = response.text
    item = ZhihuQuestionItem()

    item['name'] = re.findall(r'<meta itemprop="name" content="(.*?)"', text)[0]
    item['url'] = re.findall(r'<meta itemprop="url" content="(.*?)"', text)[0]
    item['keywords'] = re.findall(r'<meta itemprop="keywords" content="(.*?)"', text)[0]
    item['answer_count'] = re.findall(r'<meta itemprop="answerCount" content="(.*?)"', text)[0]
    item['comment_count'] = re.findall(r'<meta itemprop="commentCount" content="(.*?)"', text)[0]
    item['flower_count'] = re.findall(r'<meta itemprop="api:followerCount" content="(.*?)"', text)[0]
    item['date_created'] = re.findall(r'<meta itemprop="dateCreated" content="(.*?)"', text)[0]

    count_answer = int(item['answer_count'])
    yield item

    question_id = int(re.match(r'https://www.zhihu.com/question/(\d+)', response.url).group(1))

    # 从指定位置开始获取指定数量答案
    if count_answer > answer_count:
        count_answer = answer_count
    n = answer_offset
    while n + 20 <= count_answer:
        yield scrapy.Request(more_answer_url.format(question_id, n, n + 20), headers=headers,
                             callback=parse_answer)
        n += 20


def get_more_question(self, response):
    """ 获取更多首页问题 """
    question_url = 'https://www.zhihu.com/question/{0}'
    questions = json.loads(response.text)

    for que in questions['data']:
        question_id = re.findall(r'(\d+)', que['target']['question']['url'])[0]
        yield scrapy.Request(question_url.format(question_id), headers=headers,
                             callback=parse_question)


def parse_answer(response):
    """ 解析获取到的指定范围答案 """
    answers = json.loads(response.text)

    for ans in answers['data']:
        item = ZhihuAnswerItem()
        item['question_id'] = re.match(r'http://www.zhihu.com/api/v4/questions/(\d+)',
                                       ans['question']['url']).group(1)
        item['author'] = ans['author']['name']
        item['ans_url'] = ans['url']
        item['comment_count'] = ans['comment_count']
        item['upvote_count'] = ans['voteup_count']
        item['excerpt'] = ans['excerpt']

        yield item
