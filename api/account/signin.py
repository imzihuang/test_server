#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_token
from logic.hoodle.signin import SigninLogic

LOG = logging.getLogger(__name__)

class SigninHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        id = self.get_argument('id', '')
        _op = SigninLogic()
        continuous = _op.sign_status(id)
        if continuous > -1:
            self.finish(json.dumps({"state": 0, "continuous": continuous}))
        else:
            self.finish(json.dumps({"state": 1, "continuous": continuous}))

    @verify_token
    def post(self, user_id):
        _op = SigninLogic()
        _ = _op.user_signin(user_id)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))
