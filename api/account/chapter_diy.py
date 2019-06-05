#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_token
from logic.chapter_diy import ChapterDiyLogic

LOG = logging.getLogger(__name__)

class ChapterInfoHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        limit = int(self.get_argument('limit', "100"))
        offset = int(self.get_argument('offset', "0"))
        diy_id = self.get_argument('diy_id', '')
        user_id = self.get_argument('user_id', '')
        _op = ChapterDiyLogic()
        _ = _op.infos(id=diy_id, user_id=user_id, limit=limit, offset=offset)
        if _:
            self.finish(json.dumps(_))
        else:
            self.finish(json.dumps({'state': 1, 'message': 'query diy info error'}))

    @verify_token
    def post(self, user_id):
        boss = self.get_argument('boss', '[]')
        ball_num = int(self.get_argument('ball_num', "1"))
        barrier_indexs = self.get_argument('barrier_indexs', '[]')
        barrier_nums = self.get_argument('barrier_nums', '[]')
        barrier_types = self.get_argument('barrier_types', '[]')
        barrier_offset = self.get_argument('barrier_offset', '[]')
        nick = self.get_argument('nick', '')

        _op = ChapterDiyLogic()
        _ = _op.create(user_id, boss, ball_num, barrier_indexs, barrier_nums, barrier_types, barrier_offset, nick)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))

    @verify_token
    def put(self, user_id):
        _op = ChapterDiyLogic()
        diy_id = self.get_argument('diy_id', '')
        _ = _op.active(id=diy_id)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))
