#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from logic import Base
import logging
from db.example.max_score import MaxScoreDB
from db.example.user import UserDB

LOG = logging.getLogger(__name__)

class MaxScoreLogic(Base):
    def __init__(self):
        self.exampledb = MaxScoreDB()

    def get_score(self, user_id):
        """
        获取用户生涯最高分
        :param user_id:
        :return:
        """
        if not user_id:
            return
        userdb = UserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return
        max_score_info = self.exampledb.info_userid(user_info.id)
        if not max_score_info:
            return
        return max_score_info

    def update_by_user(self, user_id, score=0):
        if not user_id:
            return False
        userdb = UserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return False
        max_score_info = self.exampledb.info_userid(user_info.id)
        if not max_score_info:
            self.create(
                user_id=user_info.id,
                score=score,
            )
        else:
            if max_score_info.score>score:#新上传的分数比数据库中还低，异常数据
                return
            self.update(max_score_info.id, **{
                "score": score,
            })

        return True
