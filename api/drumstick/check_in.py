#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_drumstick_token
from logic.drumstick.drumstick_checkin import DrumstickCheckInLogic

LOG = logging.getLogger(__name__)

class DrumstickCheckInHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        id = self.get_argument('id', '')
        _op = DrumstickCheckInLogic()
        checkin_num = _op.get_checkin_num(id)
        if checkin_num > -1:
            self.finish(json.dumps({"state": 0, "checkin_num": checkin_num}))
        else:
            self.finish(json.dumps({"state": 1, "checkin_num": checkin_num}))

    @verify_drumstick_token
    def post(self, user_id):
        _op = DrumstickCheckInLogic()
        _ = _op.user_checkin(user_id)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))
