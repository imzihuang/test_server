#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_token
from logic.hoodle.share import ShareLogic

LOG = logging.getLogger(__name__)

class ShareHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        id = self.get_argument('id', '')
        _op = ShareLogic()
        share_num = _op.get_share_num(id)
        if share_num > -1:
            self.finish(json.dumps({"state": 0, "share_num": share_num}))
        else:
            self.finish(json.dumps({"state": 1, "share_num": share_num}))

    @verify_token
    def post(self, user_id):
        _op = ShareLogic()
        _ = _op.user_share(user_id)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))
