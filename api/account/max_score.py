#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_token
from logic.max_score import MaxScoreLogic

LOG = logging.getLogger(__name__)

class MaxScoreHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        id = self.get_argument('id', '')
        _op = MaxScoreLogic()
        max_score_info = _op.get_score(id)
        if max_score_info:
            self.finish(json.dumps({"state": 0, "score": max_score_info.score}))
        else:
            self.finish(json.dumps({"state": 1, "score": 0}))

    @verify_token
    def post(self, user_id):
        score = int(self.get_argument('score', 0))
        _op = MaxScoreLogic()
        _ = _op.update_by_user(user_id, score)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))
