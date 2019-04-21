#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_token
from logic.advertising import AdvertisingLogic

LOG = logging.getLogger(__name__)

class AdvertisingHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        id = self.get_argument('id', '')
        _op = AdvertisingLogic()
        advertising_num = _op.get_advertising_num(id)
        if advertising_num > -1:
            self.finish(json.dumps({"state": 0, "advertising_num": advertising_num}))
        else:
            self.finish(json.dumps({"state": 1, "advertising_num": advertising_num}))

    @verify_token
    def post(self, user_id):
        _op = AdvertisingLogic()
        _ = _op.user_advertising(user_id)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))
