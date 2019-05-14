#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from logic import Base
import logging
import json
from db.example.user import UserDB
LOG = logging.getLogger(__name__)

class UserLogic(Base):
    def __init__(self):
        self.exampledb = UserDB()

    def create(self, user_name="", recommend_id="",platform="",
              stance_items=[], base_items=[], book_ids=[], buy_nums=[], skill_items=[]):
        values = {
            "user_name": user_name,
            "recommend_id": recommend_id,
            "property_glod": 2000, #default
            "property_diamond": 10, #default
            "platform": platform,#平台
            "stance_items": json.dumps(stance_items),
            "base_items":json.dumps(base_items),
            "book_ids":json.dumps(book_ids),
            "buy_nums":json.dumps(buy_nums),
            "skill_items": json.dumps(skill_items),
        }

        wx_obj = self.exampledb.create(**values)
        return wx_obj

    def update_gamedata(self, id, property_glod=0,
                        property_diamond=0,
                        stance_items="",
                        base_items="",
                        book_ids="",
                        buy_nums="",
                        skill_items=""):
        if not id:
            return
        user_info = self.exampledb.info(id)
        if not user_info:
            return
        if len(user_info.book_ids)>len(book_ids) and user_info.property_glod>property_glod:
            #防止错误信息，如没有获取数据，但认证成功了，向后台写入数据
            return
        values = dict()
        if property_glod>0:
            values.update({"property_glod": property_glod})
        if property_diamond:
            values.update({"property_diamond": property_diamond})
        if stance_items:
            values.update({"stance_items": stance_items})
        if base_items:
            values.update({"base_items": base_items})
        if book_ids:
            values.update({"book_ids": book_ids})
        if buy_nums:
            values.update({"buy_nums": buy_nums})
        if skill_items:
            values.update({"skill_items": skill_items})

        _ = self.exampledb.update(user_info.id, **values)
        return _


    def infos(self, user_name="", id="", recommend_id="", limit=100, offset=1):
        offset = (offset - 1) * limit if offset > 0 else 0
        filters = dict()
        if user_name:
            filters.update({"user_name": user_name})
        if id:
            filters.update({"id": id})
        if recommend_id:
            filters.update({"recommend_id": recommend_id})
        wx_list = self.lists(offset=offset, limit=limit, **filters)
        views_list = self.views(wx_list)
        for view in views_list:
            stance_items = view.get("stance_items", [])
            view.update({"stance_items": json.loads(stance_items)})

            base_items = view.get("base_items", [])
            view.update({"base_items": json.loads(base_items)})

            book_ids = view.get("book_ids",[])
            view.update({"book_ids": json.loads(book_ids)})

            buy_nums = view.get("buy_nums",[])
            view.update({"buy_nums": json.loads(buy_nums)})

            skill_items = view.get("skill_items", [])
            view.update({"skill_items": json.loads(skill_items)})

            offline_time = self.offlineTime(view.get("updated_time", ""))
            view.update({"offline_time": offline_time})

        count = self.exampledb.counts(**filters)
        return {"count": count,
                "state": 0,
                "message": "query success",
                "data": views_list,
                "current_time": time.time()*1000#单位毫秒
                }

    def offlineTime(self, lastDate):
        """
        计算离线时间（单位秒）
        :param lastDate: 上一个日期，取用户的updated_time
        :return:
        """
        if(lastDate==""):
            return 0
        timeArray = time.strptime(lastDate, "%Y-%m-%d %H:%M:%S")
        oldTime = int(time.mktime(timeArray)) #上一次更新的时间戳
        currentTime = time.time() #当前时间戳
        return  int(currentTime - oldTime)




