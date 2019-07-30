#coding:utf-8

from tornado.web import RequestHandler
import tornado.httpclient
from six.moves.urllib import parse
from util import common_util
import logging
import json
from logic.drumstick.drumstick_wx_user import DrumstickWXUserLogic

from util.ini_client import ini_load

_conf = ini_load("config/service.ini")
game_dic_con = _conf.get_fields("drumstick_wx")

LOG = logging.getLogger(__name__)

class DrumstickWxLoginHandler(RequestHandler):
    def initialize(self, book_ids, stance_items, buy_nums, skill_items, **kwds):
        self.book_ids = book_ids
        self.stance_items = stance_items
        self.buy_nums = buy_nums
        self.skill_items = skill_items

    def post(self):
        code = self.get_argument("code", "")
        user_name = self.get_argument("user_name", "")
        recommend_id = self.get_argument("recommend_id", "")
        avatar_url = self.get_argument("avatar_url", "")

        # 微信服务器验证
        url = "https://api.weixin.qq.com/sns/jscode2session"
        app_id = game_dic_con.get("appid")
        secret = game_dic_con.get("secret")
        params = {
            "appid": app_id,
            "secret": secret,
            "js_code": code,
            "grant_type": "authorization_code"
        }
        http_client = tornado.httpclient.HTTPClient()
        response = http_client.fetch("%s?%s" % (url, parse.urlencode(params)))
        dic_body = json.loads(response.body)
        openid = dic_body.get("openid")
        session_key = dic_body.get("session_key")

        # 存储openid和session_key,并返回识别session串
        _op = DrumstickWXUserLogic()
        exit_app = _op.info_by_openid(openid=openid)
        if exit_app:
            if(exit_app.get("session_key") != session_key):
                _op.update(exit_app.get("id"), session_key=session_key)
            token = common_util.gen_token(exit_app.get("user_id"), 0)
            self.finish(json.dumps({"state": 0, "id": exit_app.get("user_id"), "token": token}))
        else:
            _ = _op.create(code=code,
                           openid=openid,
                           session_key=session_key,
                           wx_name=user_name,
                           avatar_url=avatar_url,
                           recommend_id=recommend_id,
                          )
            token = common_util.gen_token(_.get("user_id"), 0)
            self.finish(json.dumps({"state": 0, "id": _.get("user_id"), "token": token}))


