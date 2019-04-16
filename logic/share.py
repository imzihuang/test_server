#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from logic import Base
import logging
from db.example.share import ShareDB
from db.example.user import UserDB

LOG = logging.getLogger(__name__)

class ShareLogic(Base):
    def __init__(self):
        self.exampledb = ShareDB()
        super(ShareLogic, self).__init__()

    def user_share(self, id):
        if not id:
            return False
        userdb = UserDB()
        user_info = userdb.info(id)
        if not user_info:
            return False
        share_info = self.exampledb.info_userid(user_info.id)
        if not share_info:
            self.create(
                user_id=user_info.id,
                share_num= 1,
                lastdate= datetime.date.today()
            )
        else:
            if(share_info.lastdate!=datetime.date.today()):
                self.update(share_info.id, **{
                    "share_num": 1,
                    "lastdate": datetime.date.today()
                })
            else:
                self.update(share_info.id, **{
                    "share_num": share_info.share_num+1,
                    "lastdate": datetime.date.today()
                })

        return True

    def get_share_num(self, user_id):
        if not user_id:
            return -1
        userdb = UserDB()
        user_info = userdb.info(id)
        if not user_info:
            return -1
        share_info = self.exampledb.info_userid(user_info.id)
        if not share_info:
            return 0
        if(share_info.lastdate == datetime.date.today()):
            #今日分享过
            return share_info.share_num
        #未签到过
        return 0


