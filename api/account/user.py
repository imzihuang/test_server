#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_token
from logic.hoodle.user import UserLogic

LOG = logging.getLogger(__name__)

class UserHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        limit = int(self.get_argument('limit', 100))
        offset = int(self.get_argument('offset', 0))
        user_name = self.get_argument('user_name', '')
        recommend_id = self.get_argument('recommend_id', '')
        id = self.get_argument('id', '')
        _op = UserLogic()
        _value = {
            "user_name": user_name,
            "id": id,
            "recommend_id": recommend_id
        }
        _ = _op.infos(limit=limit, offset=offset, **_value)
        if _:
            self.finish(json.dumps(_))
        else:
            self.finish(json.dumps({'state': 1, 'message': 'userinfo error'}))

    @verify_token
    def put(self, user_id):
        property_glod = int(self.get_argument('property_glod', '0'))
        property_diamond = int(self.get_argument('property_diamond', '0'))
        stance_items = self.get_argument('stance_items', '[]')
        base_items = self.get_argument('base_items', '[]')
        book_ids = self.get_argument('book_ids', '[]')
        buy_nums = self.get_argument('buy_nums', '[]')
        skill_items = self.get_argument('skill_items', '[]')

        _op = UserLogic()
        _ = _op.update_gamedata(user_id,
                                property_glod=property_glod,
                                property_diamond=property_diamond,
                                stance_items=stance_items,
                                base_items=base_items,
                                book_ids=book_ids,
                                buy_nums=buy_nums,
                                skill_items = skill_items,
                                )
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))

