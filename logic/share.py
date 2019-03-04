#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from util.exception import ParamExist
from db import api as db_api
from logic import Logic
import logging

LOG = logging.getLogger(__name__)

class ShareLogic(Logic):
    def __init__(self):
        super(ShareLogic, self).__init__()

    def user_share(self, id):
        if not id:
            return False
        user_info = db_api.wxuser_get(id)
        if not user_info:
            return False
        share_info = db_api.share_get_userid(user_info.id)
        if not share_info:
            db_api.share_create({
                "user_id": user_info.id,
                "share_num": 1,
                "lastdate": datetime.date.today()
            })
        else:
            if(share_info.lastdate!=datetime.date.today()):
                db_api.share_update(share_info.id, {
                    "share_num": 1,
                    "lastdate": datetime.date.today()
                })
            else:
                db_api.share_update(share_info.id, {
                    "share_num": share_info.share_num+1,
                    "lastdate": datetime.date.today()
                })

        return True

    def get_share_num(self, user_id):
        if not user_id:
            return -1
        user_info = db_api.wxuser_get(user_id)
        if not user_info:
            return -1
        share_info = db_api.share_get_userid(user_info.id)
        if not share_info:
            return 0
        if(share_info.lastdate == datetime.date.today()):
            #今日分享过
            return share_info.share_num
        #未签到过
        return 0


