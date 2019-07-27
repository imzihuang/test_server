#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_token
from logic.hoodle.welfare import WelfareLogic

LOG = logging.getLogger(__name__)

class WelfareHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        id = self.get_argument('id', '')
        _op = WelfareLogic()
        welfare_num = _op.get_welfare_num(id)
        if welfare_num > -1:
            self.finish(json.dumps({"state": 0, "share_num": welfare_num}))
        else:
            self.finish(json.dumps({"state": 1, "share_num": welfare_num}))

    @verify_token
    def post(self, user_id):
        _op = WelfareLogic()
        _ = _op.user_welfare(user_id)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))
