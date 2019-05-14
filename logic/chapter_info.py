#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import logging
from logic import Base
from db.example.chapter_info import ChapterInfoDB

LOG = logging.getLogger(__name__)

class ChapterInfoLogic(Base):
    def __init__(self):
        self.exampledb = ChapterInfoDB()

    def infos(self):
        chapter_list = self.lists()
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

    def manage_info(self, index=0,
                    boss='[]',
                    ball_num=1,
                    barrier_indexs='[]',
                    barrier_nums='[]',
                    barrier_types='[]',
                    barrier_offset='[]'):
        if index==0:
            return
        chapter_info = self.exampledb.info_by_index(index)
        values = dict()
        values.update({"index": index})
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
        if chapter_info:
            #更新
            _ = self.exampledb.update(chapter_info.id,  **values)
            return _
        else:
            #新增，先判断index是否连续
            judge_chapter_info = self.exampledb.info_by_index(index-1)
            if not judge_chapter_info: #index不连续
                return
            _ = self.exampledb.create(**values)
            return _
