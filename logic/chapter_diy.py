#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import logging
from logic import Base
from db.example.chapter_diy import ChapterDiyDB
from db.example.user import UserDB

LOG = logging.getLogger(__name__)

class ChapterDiyLogic(Base):
    def __init__(self):
        self.exampledb = ChapterDiyDB()

    def infos(self, id="", user_id="", limit=100, offset=1):
        offset = (offset - 1) * limit if offset > 0 else 0
        filters = {}
        if id:
            filters.update({"id": id})
        if user_id:
            filters.update({"user_id": user_id})

        chapter_list = self.lists(offset=offset, limit=limit, **filters)
        views_list = self.views(chapter_list)
        for view in views_list:
            boss = view.get("boss", [])
            view.update({"boss": json.loads(boss)})

            barrier_indexs = view.get("barrier_indexs", [])
            view.update({"barrier_indexs": json.loads(barrier_indexs)})

            barrier_nums = view.get("barrier_nums", [])
            view.update({"barrier_nums": json.loads(barrier_nums)})

            barrier_types = view.get("barrier_types", [])
            view.update({"barrier_types": json.loads(barrier_types)})

            barrier_offset = view.get("barrier_offset", [])
            view.update({"barrier_offset": json.loads(barrier_offset)})
        count = self.exampledb.counts()
        return {"count": count,
                "state": 0,
                "message": "query success",
                "data": views_list,
                }

    def update_or_create(self, user_id, diy_id="", boss='[]',
                    ball_num=1,
                    barrier_indexs='[]',
                    barrier_nums='[]',
                    barrier_types='[]',
                    barrier_offset='[]',
                    nick=''):
        if not user_id:
            return
        userdb = UserDB()
        user_info = userdb.info(user_id)
        if not user_info:
            return False
        values = dict({"user_id": user_id})
        if boss:
            values.update({"boss": boss})
        if ball_num>0:
            values.update({"ball_num": ball_num})
        if barrier_indexs:
            values.update({"barrier_indexs": barrier_indexs})
        if barrier_nums:
            values.update({"barrier_nums": barrier_nums})
        if barrier_types:
            values.update({"barrier_types": barrier_types})
        if barrier_offset:
            values.update({"barrier_offset": barrier_offset})
        if nick:
            values.update({"nick": nick})
        if diy_id:
            _ = self.exampledb.update(diy_id, active=False, **values)
            return diy_id
        else:
            _ = self.exampledb.create(**values)
            return _.get("id")

    def active(self, id=""):
        if not id or id=="":
            return
        diy_info = self.exampledb.info(id)
        if not diy_info:
            return
        _ = self.exampledb.update(id, active=True)
        return _


