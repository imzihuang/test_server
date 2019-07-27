#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from logic import Base
import logging
from db.example.hoodle.welfare import WelfareDB
from db.example.hoodle.user import UserDB

LOG = logging.getLogger(__name__)

class WelfareLogic(Base):
    def __init__(self):
        self.exampledb = WelfareDB()

    def user_welfare(self, user_id):
        if not user_id:
            return False
        userdb = UserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return False
        welfare_info = self.exampledb.info_userid(user_info.id)
        if not welfare_info:
            self.create(
                user_id=user_info.id,
                welfare_num=1,
                lastdate=datetime.date.today()
            )
        else:
            if(welfare_info.lastdate!=datetime.date.today()): #新的一天
                self.update(welfare_info.id, **{
                    "welfare_num": 1,
                    "lastdate": datetime.date.today()
                })
            else:
                self.update(welfare_info.id, **{
                    "welfare_num": welfare_info.welfare_num+1,
                    "lastdate": datetime.date.today()
                })

        return True

    def get_welfare_num(self, user_id):
        if not user_id:
            return -1
        userdb = UserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return -1
        welfare_info = self.exampledb.info_userid(user_info.id)
        if not welfare_info:
            return 0
        if(welfare_info.lastdate == datetime.date.today()):
            #今日分享过
            return welfare_info.welfare_num
        #今天未玩过
        return 0


