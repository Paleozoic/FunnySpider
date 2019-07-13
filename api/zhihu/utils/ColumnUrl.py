from api.zhihu.utils.URL import URL


class ColumnUrl(URL):

    @classmethod
    def column(cls, slug):
        # 专栏
        return "https://zhuanlan.zhihu.com/api/columns/{slug}".format(slug=slug)

    @classmethod
    def column_index(cls, slug):
        # 专栏主页
        return cls.zhuanlan_host + "/{slug}".format(slug=slug)

    @classmethod
    def column_followers(cls, slug):
        # 专栏的关注者
        return cls.zhuanlan_host + "/api/columns/{slug}/followers".format(slug=slug)

    @classmethod
    def follow_column(cls, slug):
        # 关注某专栏/取消关注某专栏
        return cls.zhuanlan_host + "/api/columns/{slug}/follow".format(slug=slug)

    unfollow_column = follow_column
