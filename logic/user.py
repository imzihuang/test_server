#!/usr/bin/python
# -*- coding: utf-8 -*-

from util.exception import ParamExist
from db import api as db_api
from logic import Logic
import logging
import json
LOG = logging.getLogger(__name__)

class WXUserLogic(Logic):
    def __init__(self):
        super(WXUserLogic, self).__init__()

    def input(self, code="", openid="", session_key="", user_name="", recommend_id="",
              stance_items=dict(),base_data=[],book_ids=[]):
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
            "recommend_id": recommend_id,
            "property_glod": 100, #default
            "property_diamond": 10, #default
            "stance_items": json.dumps(stance_items),
            "base_data":json.dumps(base_data),
            "book_ids":json.dumps(book_ids)
        }

        wx_obj = db_api.wxuser_create(values)
        return wx_obj

    def update(self, id="", **kwargs):
        if not id or not kwargs:
            return False
        _ = db_api.wxuser_update(id, kwargs)
        return _

    def update_gamedata(self, session_key, property_glod=0,
                        property_diamond=0,
                        stance_items="{}",
                        base_data="[]",
                        book_ids="[]"):
        if not session_key:
            return
        user_info = db_api.wxuser_get_session_key(session_key)
        if not user_info:
            return
        stance_items = json.loads(stance_items)
        base_data = json.loads(base_data)
        book_ids = json.loads(book_ids)
        values = dict()
        if property_glod>0:
            values.update({"property_glod": property_glod})
        if property_diamond:
            values.update({"property_diamond": property_diamond})
        if stance_items:
            values.update({"stance_items": stance_items})
        if base_data:
            values.update({"base_data": base_data})
        if book_ids:
            values.update({"book_ids": book_ids})
        _ = db_api.wxuser_update(user_info.id, values)
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
            stance_items = view.get("stance_items")
            view.update({"stance_items": json.loads(stance_items)})

            base_data = view.get("base_data")
            view.update({"base_data": json.loads(base_data)})

            book_ids = view.get("book_ids")
            view.update({"book_ids": json.loads(book_ids)})

        wx_count = db_api.wxuser_count(**filters)
        return {"count": wx_count, "state": 0, "message": "query success", "data": wx_list}


    def info_by_openid(self, openid):
        if not openid:
            return
        wx_infos = db_api.wxuser_list(openid=openid)
        if wx_infos:
            return self.views(wx_infos[0])

    def info_recommend(self, session_key, limit=100, offset=1):
        """
        获取推荐人
        :param session_key:
        :return:
        """
        if not session_key:
            return
        user_info = db_api.wxuser_get_session_key(session_key)
        if not user_info:
            return {"count": 0, "state": 0, "message": "query success", "data": []}
        wx_list = db_api.wxuser_list(offset=offset, limit=limit, recommend_id=user_info.id)
        wx_count = db_api.wxuser_count(recommend_id=user_info.id)
        return {"count": wx_count, "state": 0, "message": "query success", "data": self.views(wx_list)}

    def delete(self, id="", **kwargs):
        if not id:
            return "id is none"
        db_api.wxuser_deleted(id=id)