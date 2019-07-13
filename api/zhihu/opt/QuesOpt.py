import os
import urllib
import logging
from api.zhihu import Zhihu
from api.zhihu.opt import AnsOpt


def download_imgs(zhihu: Zhihu, question_id, offset, limit, img_path):
    # 创建文件夹
    dir = os.path.join(img_path, str(question_id))
    if not os.path.exists(dir):
        os.makedirs(dir)

    answers = zhihu.get_answers(question_id=question_id, offset=offset, limit=limit)
    """
    data:
    paging:{
        is_end:true
        is_start:false
        next: xxx url
        previous: xxx url
        totals:13
    }
    """
    data = answers['data']
    for i in range(len(data)):
        """
           author:{
               name:"",
               content:"",
           }
        """
        answer = data[i]
        urls = AnsOpt.get_img_urls(answer['content'])
        # 去重，可能是正则问题，提取了重复数据。暂时不管。
        urls = list(set(urls))
        if urls:
            for j in range(len(urls)):
                try:
                    arr = urls[j].split('.')
                    file_name = str(offset).zfill(5) + "-" + str(i).zfill(5) + "-" + str(j).zfill(5) + "-" + \
                                answer['author']['name'] + "." + arr[len(arr) - 1]
                    f = open(os.path.join(dir, file_name), 'wb')
                    # 打印url
                    logging.info(urls[j])
                    f.write((urllib.request.urlopen("https://" + urls[j])).read())
                except Exception as e:
                    logging.error("[ERROR===>>>]无法写入文件！", e)
                finally:
                    f.close()
    return answers['paging']
