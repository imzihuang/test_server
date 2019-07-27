#coding:utf-8

from tornado.web import RequestHandler
import tornado.httpclient
from six.moves.urllib import parse
import logging
import json
from util.hmac_256 import get_sign
from logic.hoodle.wx_user import WXUserLogic
from util.ini_client import ini_load

_conf = ini_load('config/service.ini')
game_dic_con = _conf.get_fields('game_wx')

LOG = logging.getLogger(__name__)

class StorageHandler(RequestHandler):
    def post(self):
        user_id = self.get_argument('user_id', '')
        maxScore = self.get_argument('maxScore', '')
        wx_op = WXUserLogic()
        wx_userinfo = wx_op.info_by_userid(user_id=user_id)
        code = wx_userinfo.get("code")
        #_ = self.login(code)
        #openid, session_key = _
        openid = wx_userinfo.get("openid")
        session_key = wx_userinfo.get("session_key")
        access_token = self.get_token()
        body_params = '{ "kv_list":[{"key":"maxScore","value":"'+maxScore+'"}, {"key": "score", "value": "0"}] }'
        signature = get_sign(body_params, session_key)
        params = {
            "access_token": access_token,
            "openid": openid,
            "signature": signature,
            "sig_method": "hmac_sha256",
        }
        LOG.info(params)
        http_client = tornado.httpclient.HTTPClient()
        url = "https://api.weixin.qq.com/wxa/set_user_storage"
        response = http_client.fetch("%s?%s" % (url, parse.urlencode(params)), method='POST', body=body_params)
        self.finish(json.dumps({'state': 0, "body":response.body}))

    def login(self, code):
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
        LOG.info(response)
        dic_body = json.loads(response.body)
        openid = dic_body.get('openid')
        session_key = dic_body.get('session_key')
        return openid, session_key

    def get_token(self):
        token_url = "https://api.weixin.qq.com/cgi-bin/token"#&appid=APPID&secret=APPSECRET"
        app_id = game_dic_con.get("appid")
        secret = game_dic_con.get("secret")
        params = {
            "appid": app_id,
            "secret": secret,
            "grant_type": "client_credential"
        }
        http_client = tornado.httpclient.HTTPClient()
        response = http_client.fetch("%s?%s" % (token_url, parse.urlencode(params)))
        dic_body = json.loads(response.body)
        access_token = dic_body.get('access_token')
        return access_token

