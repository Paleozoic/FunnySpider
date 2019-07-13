import re


# 提取知乎回答内容的图片url
def get_img_urls(content):
    urls = find_url(content)
    return urls



def find_url(string):
    # findall() 查找匹配正则表达式的字符串 data-original 原始图片
    url = re.findall('data-original=\\"https://(.*?)\\"', string)
    return url