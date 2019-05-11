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

    def get_chapter_num(self, user_id):
        """
        获取用户通关得关卡
        :param user_id:
        :return:
        """
        if not user_id:
            return -1
        userdb = UserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return -1
        chapter_info = self.exampledb.info_userid(user_info.id)
        if not chapter_info:
            return 0
        return chapter_info.chapter_num

    def update_by_user(self, user_id, chapter_num=0):
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
                chapter_num=chapter_num
            )
        else:
            if chapter_info.chapter_num<chapter_num:#只有突破了更高得关卡才更新
                self.update(chapter_info.id, **{
                    "chapter_num": chapter_num,
                })
        return True
