#!/usr/bin/python
# -*- coding: utf-8 -*-


from util import convert
from util.exception import ParamExist
from db import api as db_api
from logic import Logic
import logging
LOG = logging.getLogger(__name__)

class MonsterLogic(Logic):
    def __init__(self):
        super(MonsterLogic, self).__init__()


    def infos(self, id="", monster_name="", limit=100, offset=1):
        offset = (offset - 1) * limit if offset > 0 else 0
        filters = dict()

        if id:
            filters.update({"id": id})
        if monster_name:
            filters.update({"monster_name": monster_name})
        monster_list = db_api.monster_list(offset=offset, limit=limit, **filters)

        monster_count = db_api.monster_count(**filters)
        return {"count": monster_count, "state": 0, "message": "query success", "data": self.views(monster_list)}

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