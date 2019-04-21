#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from logic import Base
import logging
from db.example.advertising import AdvertisingDB
from db.example.user import UserDB

LOG = logging.getLogger(__name__)

class AdvertisingLogic(Base):
    def __init__(self):
        self.exampledb = AdvertisingDB()

    def user_advertising(self, user_id):
        if not user_id:
            return False
        userdb = UserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return False
        advertising_info = self.exampledb.info_userid(user_info.id)
        if not advertising_info:
            self.create(
                user_id=user_info.id,
                advertising_num= 1,
                lastdate= datetime.date.today()
            )
        else:
            if(advertising_info.lastdate!=datetime.date.today()):
                self.update(advertising_info.id, **{
                    "advertising_num": 1,
                    "lastdate": datetime.date.today()
                })
            else:
                self.update(advertising_info.id, **{
                    "advertising_num": advertising_info.advertising_num+1,
                    "lastdate": datetime.date.today()
                })

        return True

    def get_advertising_num(self, user_id):
        if not user_id:
            return -1
        userdb = UserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return -1
        advertising_info = self.exampledb.info_userid(user_info.id)
        if not advertising_info:
            return 0
        if(advertising_info.lastdate == datetime.date.today()):
            #今日分享过
            return advertising_info.advertising_num
        #未签到过
        return 0


