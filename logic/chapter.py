#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from logic import Base
import logging
from db.example.chapter import ChapterDB
from db.example.user import UserDB

LOG = logging.getLogger(__name__)

class ChapterLogic(Base):
    def __init__(self):
        self.exampledb = ChapterDB()

    def get_chapter(self, user_id):
        """
        获取用户通关得关卡
        :param user_id:
        :return:
        """
        if not user_id:
            return
        userdb = UserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return
        chapter_info = self.exampledb.info_userid(user_info.id)
        if not chapter_info:
            return
        return chapter_info

    def update_by_user(self, user_id, chapter_num=0, not_pass=''):
        if not user_id:
            return False
        userdb = UserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return False
        chapter_info = self.exampledb.info_userid(user_info.id)
        if not chapter_info:
            self.create(
                user_id=user_info.id,
                chapter_num=chapter_num,
                not_pass = not_pass,
            )
        else:
            not_pass_list = not_pass.split(',')
            if(len(not_pass_list)>0):
                for not_p in not_pass_list:
                    if int(not_p)>=chapter_num: #未通关比最高通关关卡还高，异常数据
                        return False
            if chapter_info.chapter_num>chapter_num:#新上传的最高关卡比数据库中还低，异常数据
                return
            self.update(chapter_info.id, **{
                "chapter_num": chapter_num,
                "not_pass": not_pass
            })

        return True
