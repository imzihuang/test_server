#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_token
from logic.drumstick.drumstick_user import DrumstickUserLogic

LOG = logging.getLogger(__name__)

class DrumstickUserHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        limit = int(self.get_argument("limit", "100"))
        offset = int(self.get_argument("offset", "0"))
        user_name = self.get_argument("user_name", "")
        recommend_id = self.get_argument("recommend_id", "")
        id = self.get_argument("id", "")
        _op = DrumstickUserLogic()
        _value = {
            "user_name": user_name,
            "id": id,
            "recommend_id": recommend_id
        }
        _ = _op.infos(limit=limit, offset=offset, **_value)
        if _:
            self.finish(json.dumps(_))
        else:
            self.finish(json.dumps({"state": 1, "message": "userinfo error"}))

    @verify_token
    def put(self, user_id):
        glod = int(self.get_argument("glod", "0"))
        diamond = int(self.get_argument("diamond", "0"))
        hero_items = self.get_argument("hero_items", "[]")
        map_items = self.get_argument("map_items", "[]")
        current_hero_id = self.get_argument("current_hero_id", "")


        _op = DrumstickUserLogic()
        _ = _op.update_gamedata(user_id,
                                glod=glod,
                                diamond=diamond,
                                hero_items=hero_items,
                                map_items=map_items,
                                current_hero_id=current_hero_id,
                                )
        if _:
            self.finish(json.dumps({"state": 0}))
        else:
            self.finish(json.dumps({"state": 1}))

