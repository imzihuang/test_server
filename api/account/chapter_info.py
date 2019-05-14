#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_token
from logic.chapter_info import ChapterInfoLogic

LOG = logging.getLogger(__name__)

class ChapterInfoHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        _op = ChapterInfoLogic()
        _ = _op.infos()
        if _:
            self.finish(json.dumps(_))
        else:
            self.finish(json.dumps({'state': 1, 'message': 'query all chapter info error'}))

    @verify_token
    def post(self, user_id):
        index = int(self.get_argument('index', 0))
        boss = self.get_argument('boss', '[]')
        ball_num = int(self.get_argument('ball_num', 1))
        barrier_indexs = self.get_argument('barrier_indexs', '[]')
        barrier_nums = self.get_argument('barrier_nums', '[]')
        barrier_types = self.get_argument('barrier_types', '[]')
        barrier_offset = self.get_argument('barrier_offset', '[]')

        _op = ChapterInfoLogic()
        _ = _op.manage_info(index, boss, ball_num, barrier_indexs, barrier_nums, barrier_types, barrier_offset)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))
