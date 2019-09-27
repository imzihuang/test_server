#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from logic import Base
import logging
import json
from db.example.drumstick.drumstick_user import DrumstickUserDB
LOG = logging.getLogger(__name__)

class DrumstickUserLogic(Base):
    def __init__(self):
        self.exampledb = DrumstickUserDB()

    def create(self, user_name="", recommend_id="", avatar_url=""):
        values = {
            "user_name": user_name,
            "recommend_id": recommend_id,
            "glod": 40000, #default
            "diamond": 400, #default
            "avatar_url": avatar_url,
            "hero_items": json.dumps([{"h_id": "h001", "lvl": 1, "max_lvl": 2}, {"h_id": "h002", "lvl": 1, "max_lvl": 2}]),
            "map_items": json.dumps(["m001", "m002"]),
            "prop_items": json.dumps([{"id":"s001", "num":1}, {"id":"s002", "num":1},{"id":"s003", "num":1}, {"id":"s004", "num":1}]),
            "current_hero_id": "h001",
            "current_map_id": "m001",
        }

        wx_obj = self.exampledb.create(**values)
        return wx_obj

    def update_gamedata(self, id, glod=-1,
                        diamond=-1,
                        avatar_url="",
                        hero_items="",
                        map_items="",
                        prop_items = "",
                        current_hero_id="",
                        current_map_id="",
                        kill_enemy=0,
                        max_lift=0,
                        lift_lvl1=0,
                        lift_lvl2=0,
                        lift_lvl3=0):

        if not id:
            return
        user_info = self.exampledb.info(id)
        if not user_info:
            return
        if hero_items and len(json.loads(user_info.hero_items))>len(json.loads(hero_items)):
            #防止错误信息，如没有获取数据，但认证成功了，向后台写入数据
            return
        values = dict()
        if glod>=0:
            values.update({"glod": glod})
        if diamond>=0:
            values.update({"diamond": diamond})
        if avatar_url:
            values.update({"avatar_url": avatar_url})
        if hero_items:
            values.update({"hero_items": hero_items})
        if map_items:
            values.update({"map_items": map_items})
        if prop_items:
            values.update({"prop_items": prop_items})
        if current_hero_id:
            values.update({"current_hero_id": current_hero_id})
        if current_map_id:
            values.update({"current_map_id": current_map_id})
        if kill_enemy>0:
            values.update({"kill_enemy": kill_enemy})
        if max_lift>0:
            values.update({"max_lift": max_lift})
        if lift_lvl1>0:
            values.update({"lift_lvl1": lift_lvl1})
        if lift_lvl2:
            values.update({"lift_lvl2": lift_lvl2})
        if lift_lvl3:
            values.update({"lift_lvl3": lift_lvl3})
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
        _user_list = self.lists(offset=offset, limit=limit, **filters)
        _views_list = self.views(_user_list)
        for view in _views_list:
            hero_items = view.get("hero_items", "[]")
            view.update({"hero_items": json.loads(hero_items)})

            map_items = view.get("map_items", "[]")
            view.update({"map_items": json.loads(map_items)})

            prop_items = view.get("prop_items", "[]")
            view.update({"prop_items": json.loads(prop_items)})

        count = self.exampledb.counts(**filters)
        return {"count": count,
                "state": 0,
                "message": "query success",
                "data": _views_list,
                }

    def getCountByRecommend(self, recommend_id):
        """
        获取被推荐人的总数和前一天登录的总数
        :param recommend_id: 推荐人id
        :return:
        """
        if not recommend_id:
            return {
                "no_active": [],
                "active": []
            }
        _user_list = self.lists(recommend_id= recommend_id)
        no_active = []
        active = []
        for userInfo in _user_list:
            timeArray = time.strptime(userInfo.updated_time.strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")
            oldTime = int(time.mktime(timeArray))  # 最后一次活跃时间
            currentTime = time.time()  # 当前时间戳
            if int(currentTime - oldTime)< 60*60*24*2:#2天内，算是活跃
                active.append({"avatar_url": userInfo.avatar_url})
            else:
                no_active.append({"avatar_url": userInfo.avatar_url})
        return {
            "no_active":no_active,
            "active":active
        }



