from api.zhihu.Zhihu import Zhihu

IMG_PATH = 'F:\\tmp\\'

def test_download_imgs():
    # api = Zhihu("xx", "xx")
    zhihu = Zhihu()
    question_id = 26037846
    zhihu.download_all_imgs(question_id, IMG_PATH)
