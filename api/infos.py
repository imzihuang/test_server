#coding:utf-8

from tornado.web import RequestHandler
import json
from util.convert import is_mobile
from util.exception import ParamExist
import logging

from logic import Logic

from logic.user import WXUserLogic
from logic.monster import MonsterLogic

LOG = logging.getLogger(__name__)

class InfosHandler(RequestHandler):
    def get(self, infos_obj):
        limit = int(self.get_argument('limit', 100))
        offset = int(self.get_argument('offset', 0))
        try:
            _op = Logic()
            _value = dict()

            if infos_obj == "userinfo":
                _value = self._get_user_argument()
                _op = WXUserLogic()

            if infos_obj == "monsterinfo":
                _value = self._get_monster_argument()
                _op = MonsterLogic()

            _ = _op.infos(limit=limit, offset=offset, **_value)
            if _:
                self.finish(json.dumps(_))
            else:
                self.finish(json.dumps({'state': 1, 'message': 'action %s error'%infos_obj}))
        except Exception as ex:
            LOG.error("query %s error:%s"%(infos_obj, ex))
            self.finish(json.dumps({"state":1, "message":"error", "data":[]}))


    def _get_user_argument(self):
        user_name = self.get_argument('user_name', '')
        session_key = self.get_argument('session_key', '')
        return {
            "user_name": user_name,
            "session_key": session_key
        }

    def _get_monster_argument(self):
        id = self.get_argument('id', '')
        name = self.get_argument('name', '')
        return {
            "id": id,
            "monster_name": name
        }


