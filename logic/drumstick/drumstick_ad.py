#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from logic import Base
import logging
from db.example.drumstick.drumstick_ad import DrumstickAdDB
from db.example.drumstick.drumstick_user import DrumstickUserDB

LOG = logging.getLogger(__name__)

class DrumstickAdLogic(Base):
    def __init__(self):
        self.exampledb = DrumstickAdDB()

    def user_ad(self, user_id):
        """
        广告计数
        :param user_id:
        :return:
        """
        if not user_id:
            return False
        userdb = UserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return False
        ad_info = self.exampledb.info_userid(user_info.id)
        if not ad_info:
            self.create(
                user_id=user_info.id,
                advertising_num= 1,
                lastdate= datetime.date.today()
            )
        else:
            if(ad_info.lastdate!=datetime.date.today()):
                self.update(ad_info.id, **{
                    "advertising_num": 1,
                    "lastdate": datetime.date.today()
                })
            else:
                self.update(ad_info.id, **{
                    "advertising_num": ad_info.advertising_num+1,
                    "lastdate": datetime.date.today()
                })

        return True

    def get_ad_num(self, user_id):
        if not user_id:
            return -1
        userdb = DrumstickUserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return -1
        ad_info = self.exampledb.info_userid(user_info.id)
        if not ad_info:
            return 0
        if(ad_info.lastdate == datetime.date.today()):
            #今日广告次数
            return ad_info.advertising_num
        #未签到过
        return 0


