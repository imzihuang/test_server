#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from util.exception import ParamExist
from db import api as db_api
from logic import Logic
import logging

LOG = logging.getLogger(__name__)

class SigninLogic(Logic):
    def __init__(self):
        super(SigninLogic, self).__init__()

    def user_signin(self, session_key):
        if not session_key:
            return False
        user_info = db_api.wxuser_get_session_key(session_key)
        if not user_info:
            return False
        sign_info = db_api.signin_get_userid(user_info.id)
        if not sign_info:
            db_api.signin_create({
                "user_id": user_info.id,
                "continuous": 1,
                "lastdate": datetime.date.today()
            })
        else:
            continuous = sign_info.continuous+1 if sign_info.continuous<7 else 1
            db_api.signin_update(sign_info.id, {
                "continuous": continuous,
                "lastdate": datetime.date.today()
            })

        return True

    def sign_status(self, session_key):
        if not session_key:
            return -1
        user_info = db_api.wxuser_get_session_key(session_key)
        if not user_info:
            return -1
        sign_info = db_api.signin_get_userid(user_info.id)
        if(sign_info.lastdate == datetime.date.today()):
            #今日签到过
            return sign_info.continuous
        #未签到过
        return 0


