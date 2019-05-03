#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_token
from logic.chapter import ChapterLogic

LOG = logging.getLogger(__name__)

class ChapterHandler(RequestHandler):
    def initialize(self, **kwds):
        pass

    def get(self):
        id = self.get_argument('id', '')
        _op = ChapterLogic()
        chapter_num = _op.get_chapter_num(id)
        if chapter_num > -1:
            self.finish(json.dumps({"state": 0, "chapter_num": chapter_num}))
        else:
            self.finish(json.dumps({"state": 1, "chapter_num": chapter_num}))

    @verify_token
    def post(self, user_id):
        chapter_num = int(self.get_argument('chapter_num', 0))
        _op = ChapterLogic()
        _ = _op.update_by_user(user_id, chapter_num)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))
