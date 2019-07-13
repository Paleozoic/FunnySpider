from api.zhihu.utils.URL import URL


# 提取知乎回答内容的图片url
def get_img_urls(content):
    urls = URL.find_url(content)
    return urls
