#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_drumstick_token
from logic.drumstick.drumstick_ad import DrumstickAdLogic

LOG = logging.getLogger(__name__)

class DrumstickAdHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        id = self.get_argument('id', '')
        _op = DrumstickAdLogic()
        advertising_num = _op.get_ad_num(id)
        if advertising_num > -1:
            self.finish(json.dumps({"state": 0, "advertising_num": advertising_num}))
        else:
            self.finish(json.dumps({"state": 1, "advertising_num": advertising_num}))

    @verify_drumstick_token
    def post(self, user_id):
        _op = DrumstickAdLogic()
        _ = _op.user_ad(user_id)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))
