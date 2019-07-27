#!/usr/bin/python
# -*- coding: utf-8 -*-

from util.exception import ParamExist
from logic import Base
import logging
import json
from db.example.drumstick.drumstick_user import DrumstickUserDB
from db.example.drumstick.drumstick_wx_user import DrumstickWxUserDB
LOG = logging.getLogger(__name__)

class DrumstickWXUserLogic(Base):
    def __init__(self):
        self.exampledb = DrumstickWxUserDB()

    def create(self, code="", openid="", session_key="", wx_name="", recommend_id=""):
        if self.lists(openid=openid):
            raise ParamExist(openid=openid)

        if self.lists(session_key=session_key):
            raise ParamExist(session_key=session_key)

        userdb = DrumstickUserDB()
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
            "glod": 2000, #default
            "diamond": 10, #default
            "hero_items": json.dumps([{"h_id": "h001", "lvl": 1, "max_lvl": 2}]),
            "map_items": json.dumps(["m001", "m002"]),
            "current_hero_id": "h001",
        }

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
