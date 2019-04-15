#coding:utf-8

from tornado.web import RequestHandler
import tornado.httpclient
from six.moves.urllib import parse
from util.exception import ParamExist
import logging
import json
from api.base import verify_token
from util import common_util
from logic.user import WXUserLogic
from logic.signin import SigninLogic
from logic.share import ShareLogic

from util.ini_client import ini_load

_conf = ini_load('config/service.ini')
game_dic_con = _conf.get_fields('game_wx')

LOG = logging.getLogger(__name__)


class WXActionHandler(RequestHandler):
    def initialize(self, book_ids, stance_items, buy_nums, **kwds):
        self.book_ids = book_ids
        self.stance_items = stance_items
        self.buy_nums = buy_nums

    def post(self, action):
        try:
            if action == "login":
                self.login()
            if action == "update_gamedata":
                self.update_gamedata()
            if action == "signin":
                self.signin()
            if action == "share":
                self.share()
        except ParamExist as ex:
            LOG.error("Wx action %s error:%s" % (action, ex))
            self.finish(json.dumps({'state': 9, 'message': 'params exit'}))
        except Exception as ex:
            LOG.error("Wx action %s error:%s" % (action, ex))
            self.finish(json.dumps({'state': 10, 'message': 'wx action error'}))

    def login(self):#//注册或登录
        code = self.get_argument('code', '')
        user_name = self.get_argument('user_name', '')
        recommend_id = self.get_argument('recommend_id', '')
        platform = self.get_argument('platform', 'wx') #游戏平台

        #微信服务器验证
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
        response = http_client.fetch("%s?%s"%(url, parse.urlencode(params)))
        dic_body = json.loads(response.body)
        openid = dic_body.get('openid')
        session_key = dic_body.get('session_key')

        #存储openid和session_key,并返回识别session串
        _op = WXUserLogic()
        exit_app = _op.info_by_openid(openid=openid)
        if exit_app and exit_app.get("session_key")!=session_key:
            _op.update(exit_app.get("id"), session_key=session_key)
            token = common_util.gen_token(exit_app.get("id"), 0)
            self.finish(json.dumps({'state': 0, 'id': exit_app.get("id"), 'token': token}))
        else:
            _ = _op.input(code=code,
                          openid=openid,
                          session_key=session_key,
                          user_name=user_name,
                          recommend_id=recommend_id,
                          platform=platform,
                          stance_items=self.stance_items,
                          book_ids=self.book_ids,
                          buy_nums=self.buy_nums,
                          )
            token = common_util.gen_token(_.get("id"), 0)
            self.finish(json.dumps({'state': 0, 'id': _.get("id"), 'token': token}))

    @verify_token
    def signin(self, user_id):#签到
        #id = self.get_argument('id', '')
        _op = SigninLogic()
        _ = _op.user_signin(user_id)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))

    @verify_token
    def update_gamedata(self, user_id):
        #id = self.get_argument('id', '')
        #LOG.info("user id:"+user_id)
        property_glod = int(self.get_argument('property_glod', 0))
        property_diamond = int(self.get_argument('property_diamond', 0))
        stance_items = self.get_argument('stance_items', '{}')
        base_items = self.get_argument('base_items', '[]')
        book_ids = self.get_argument('book_ids', '[]')
        buy_nums = self.get_argument('buy_nums', '[]')

        _op = WXUserLogic()
        _ = _op.update_gamedata(user_id,
                                property_glod = property_glod,
                                property_diamond = property_diamond,
                                stance_items = stance_items,
                                base_items=base_items,
                                book_ids=book_ids,
                                buy_nums=buy_nums,
                                )
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))

    @verify_token
    def share(self, user_id):
        #id = self.get_argument('id', '')
        _op = ShareLogic()
        _ = _op.user_share(id)
        if _:
            self.finish(json.dumps({'state': 0}))
        else:
            self.finish(json.dumps({'state': 1}))


