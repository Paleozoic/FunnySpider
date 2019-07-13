from api.zhihu.utils.URL import URL


class AnsUrl(URL):

    @classmethod
    def vote_up(cls, answer_id):
        # 赞同/反对/中立
        return cls.host + "/api/v4/answers/{id}/voters".format(id=answer_id)

    vote_down = vote_neutral = vote_up

    @classmethod
    def thank(cls, answer_id):
        # 某答案下感谢答主/取消感谢
        return cls.host + "/api/v4/answers/{id}/thankers".format(id=answer_id)

    thank_cancel = thank

    @classmethod
    def nothelp(cls, answer_id):
        # 某答案没有帮助/撤销没有帮助
        return cls.host + "/api/v4/answers/{id}/unhelpers".format(id=answer_id)

    nothelp_cancel = nothelp

    @classmethod
    def answers(cls, question_id, offset, limit):
        # https://github.com/YaoZeyuan/ZhihuHelp/issues/89
        include = "data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question.detail,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics"
        platform = "desktop"
        sort_by = "default"
        url = cls.host + "/api/v4/questions/{question_id}/answers?include={include}&limit={limit}&offset={offset}&platform={platform}&sort_by={sort_by}".format(
            question_id=question_id, include=include, limit=limit, offset=offset, platform=platform, sort_by=sort_by)
        return url
