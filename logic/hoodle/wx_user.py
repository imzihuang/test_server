#!/usr/bin/python
# -*- coding: utf-8 -*-

from util.exception import ParamExist
from logic import Base
import logging
import json
from db.example.hoodle.wx_user import WxUserDB
from db.example.hoodle.user import UserDB
LOG = logging.getLogger(__name__)

class WXUserLogic(Base):
    def __init__(self):
        self.exampledb = WxUserDB()

    def create(self, code="", openid="", session_key="", wx_name="", recommend_id="",platform="",
              stance_items=[], base_items=[], book_ids=[], buy_nums=[], skill_items=[]):
        if self.lists(openid=openid):
            raise ParamExist(openid=openid)

        if self.lists(session_key=session_key):
            raise ParamExist(session_key=session_key)

        userdb = UserDB()
        #简单兼容
        if recommend_id and not userdb.info(recommend_id):
            recommend_id = ""

        wx_user_values={
            "code": code,
            "openid": openid,
            "session_key": session_key,
            "wx_name": wx_name,
        }

        user_values = {
            "user_name": wx_name,
            "recommend_id": recommend_id,
            "property_glod": 2000, #default
            "property_diamond": 10, #default
            "platform": platform,#平台
            "stance_items": json.dumps(stance_items),
            "base_items":json.dumps(base_items),
            "book_ids":json.dumps(book_ids),
            "buy_nums":json.dumps(buy_nums),
            "skill_items": json.dumps(skill_items)
        }

        userdb = UserDB()
        user_info = userdb.create(**user_values)
        wx_userInfo = self.exampledb.create(user_id=user_info.get("id"), **wx_user_values)
        return wx_userInfo

    def info_by_openid(self, openid):
        if not openid:
            return
        wx_infos = self.lists(openid=openid)
        if wx_infos:
            return self.views(wx_infos[0])

    def info_by_userid(self, user_id):
        if not user_id:
            return
        wx_infos = self.lists(user_id=user_id)
        if wx_infos:
            return self.views(wx_infos[0])
