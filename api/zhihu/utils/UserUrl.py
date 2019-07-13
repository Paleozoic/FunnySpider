from api.zhihu.utils.URL import URL


class UserUrl(URL):

    @classmethod
    def message(cls):
        # 私信
        return cls.host + "/api/v4/messages"

    @classmethod
    def profile(cls, user_slug):
        # 用户信息
        return cls.host + "/api/v4/members/{user_slug}".format(user_slug=user_slug)

    @classmethod
    def follow_people(cls, user_slug):
        # 关注用户
        return cls.host + "/api/v4/members/{user_slug}/followers".format(user_slug=user_slug)

    @classmethod
    def followers(cls, user_slug):
        # 粉丝列表URL
        return cls.host + "/api/v4/members/{slug}/followers?include=data[*].answer_count,gender,follower_count," \
                          "badge[?(type=best_answerer)].topics".format(slug=user_slug)
