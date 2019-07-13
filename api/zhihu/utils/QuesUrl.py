from api.zhihu.utils.URL import URL


class QuesUrl(URL):

    @classmethod
    def follow_question(cls, question_id):
        # 关注某问题/取消关注某问题
        return cls.host + "/api/v4/questions/{id}/followers".format(id=question_id)

    unfollow_question = follow_question
