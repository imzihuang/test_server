#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from logic import Base
import logging
from db.example.signin import SigninDB
from db.example.user import UserDB

LOG = logging.getLogger(__name__)

class SigninLogic(Base):
    def __init__(self):
        self.exampledb = SigninDB()

    def user_signin(self, id):
        if not id:
            return False
        userdb = UserDB()
        user_info = userdb.info(id)
        if not user_info:
            return False
        sign_info = self.exampledb.info_userid(user_info.id)
        if not sign_info:
            self.create(**{
                "user_id": user_info.id,
                "continuous": 1,
                "lastdate": datetime.date.today()
            })
        else:
            continuous = sign_info.continuous+1 if sign_info.continuous<7 else 1
            self.update(sign_info.id, **{
                "continuous": continuous,
                "lastdate": datetime.date.today()
            })

        return True

    def sign_status(self, id):
        if not id:
            return -1
        userdb = UserDB()
        user_info = userdb.info(id)
        if not user_info:
            return -1
        sign_info = self.exampledb.info_userid(user_info.id)
        if(sign_info.lastdate == datetime.date.today()):
            #今日签到过
            return sign_info.continuous
        #未签到过
        return 0


