#!/usr/bin/python
# -*- coding: utf-8 -*-


from util import convert
from util.exception import ParamExist
from db import api as db_api
from logic import Logic
import logging
LOG = logging.getLogger(__name__)

class WXUserLogic(Logic):
    def __init__(self):
        super(WXUserLogic, self).__init__()

    def input(self, code="", openid="", session_key="", user_name="", recommend_id=""):
        if db_api.wxuser_list(openid=openid):
            raise ParamExist(openid=openid)

        if db_api.wxuser_list(session_key=session_key):
            raise ParamExist(session_key=session_key)

        #简单兼容
        if recommend_id and not db_api.wxuser_get(recommend_id):
            recommend_id = ""

        values = {
            "code": code,
            "openid": openid,
            "session_key": session_key,
            "user_name": user_name,
            "recommend_id": recommend_id
        }

        wx_obj = db_api.wxuser_create(values)
        return wx_obj

    def update(self, id="", **kwargs):
        if not id or not kwargs:
            return False
        _ = db_api.wxuser_update(id, kwargs)
        return _

    def infos(self, user_name="", session_key="", limit=100, offset=1):
        offset = (offset - 1) * limit if offset > 0 else 0
        filters = dict()

        if user_name:
            filters.update({"user_name": user_name})
        if session_key:
            filters.update({"session_key": session_key})
        wx_list = db_api.wxuser_list(offset=offset, limit=limit, **filters)
        #获取所拥有的怪物信息 monsterdata
        views_list = self.views(wx_list)
        for view in views_list:
            monsterdata = db_api.usermonster_list(user_id=view.get("id"))
            view.update({"monsterdata": self.views(monsterdata)})

        wx_count = db_api.wxuser_count(**filters)
        return {"count": wx_count, "state": 0, "message": "query success", "data": wx_list}


    def info_by_openid(self, openid):
        if not openid:
            return
        wx_infos = db_api.wxuser_list(openid=openid)
        if wx_infos:
            return self.views(wx_infos[0])

    def delete(self, id="", **kwargs):
        if not id:
            return "id is none"
        db_api.wxuser_deleted(id=id)