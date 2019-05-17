#coding:utf-8

from tornado.web import RequestHandler
import logging
import json
from api.base import verify_token

LOG = logging.getLogger(__name__)

class NoticeHandler(RequestHandler):
    def initialize(self, notice_content, notice_version, **kwds):
        self.notice_content = notice_content
        self.notice_version = notice_version

    def get(self):
        self.finish(json.dumps({"state": 0, "version": self.notice_version, "content": self.notice_content}))
