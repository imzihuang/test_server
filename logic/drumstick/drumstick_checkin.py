#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from logic import Base
import logging
from db.example.drumstick.drumstick_checkin import DrumstickCheckInDB
from db.example.drumstick.drumstick_user import DrumstickUserDB

LOG = logging.getLogger(__name__)

class DrumstickCheckInLogic(Base):
    def __init__(self):
        self.exampledb = DrumstickCheckInDB()

    def user_checkin(self, user_id):
        """
        签到计数
        :param user_id:
        :return:
        """
        if not user_id:
            return False
        userdb = DrumstickUserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return False
        checkin_info = self.exampledb.info_userid(user_info.id)
        if not checkin_info:
            self.create(
                user_id=user_info.id,
                checkin_num= 1,
                lastdate= datetime.date.today()
            )
        else:
            if(checkin_info.lastdate!=datetime.date.today()):
                self.update(checkin_info.id, **{
                    "checkin_num": 1,
                    "lastdate": datetime.date.today()
                })
            else:
                self.update(checkin_info.id, **{
                    "checkin_num": checkin_info.checkin_num+1,
                    "lastdate": datetime.date.today()
                })

        return True

    def get_checkin_num(self, user_id):
        if not user_id:
            return -1
        userdb = DrumstickUserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return -1
        checkin_info = self.exampledb.info_userid(user_info.id)
        if not checkin_info:
            return 0
        if(checkin_info.lastdate == datetime.date.today()):
            #今日签到次数
            return checkin_info.checkin_num
        #未签到过
        return 0


