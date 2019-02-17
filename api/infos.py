#coding:utf-8

from tornado.web import RequestHandler
import json
import logging

from logic.user import WXUserLogic
from logic.signin import SigninLogic

LOG = logging.getLogger(__name__)

class InfosHandler(RequestHandler):
    def get(self, infos_obj):
        try:
            if infos_obj == "userinfo":
                self.userinfo()

            if infos_obj == "recommend":
                self.recommend()

            if infos_obj == "signin_status":
                self.signin_status()

        except Exception as ex:
            LOG.error("query %s error:%s"%(infos_obj, ex))
            self.finish(json.dumps({"state":1, "message":"error", "data":[]}))

    def userinfo(self):
        limit = int(self.get_argument('limit', 100))
        offset = int(self.get_argument('offset', 0))
        user_name = self.get_argument('user_name', '')
        id = self.get_argument('id', '')
        _op = WXUserLogic()
        _value = {
            "user_name": user_name,
            "id": id
        }
        _= _op.infos(limit=limit, offset=offset, **_value)
        if _:
            self.finish(json.dumps(_))
        else:
            self.finish(json.dumps({'state': 1, 'message': 'userinfo error'}))

    def recommend(self):
        limit = int(self.get_argument('limit', 100))
        offset = int(self.get_argument('offset', 0))
        id = self.get_argument('id', '')
        _op = WXUserLogic()
        _ = _op.info_recommend(id, limit=limit, offset=offset)
        if _:
            self.finish(json.dumps(_))
        else:
            self.finish(json.dumps({'state': 1, 'message': 'recommend error'}))

    def signin_status(self):
        id = self.get_argument('id', '')
        _op = SigninLogic()
        continuous = _op.sign_status(id)
        if continuous>-1:
            self.finish(json.dumps({"state": 0, "continuous": continuous}))
        else:
            self.finish(json.dumps({"state": 1, "continuous": continuous}))

