#coding:utf-8

from tornado.web import RequestHandler
import tornado.httpclient
from six.moves.urllib import parse
from util.exception import ParamExist
import logging
import json
from logic.user import WXUserLogic

from util.ini_client import ini_load

_conf = ini_load('config/service.ini')
relative_dic_con = _conf.get_fields('relative_wx')
teacher_dic_con = _conf.get_fields('teacher_wx')

LOG = logging.getLogger(__name__)


class WXActionHandler(RequestHandler):

    def post(self, action):
        try:
            if action == "login":
                self.login()
                return
        except ParamExist as ex:
            LOG.error("Wx action %s error:%s" % (action, ex))
            self.finish(json.dumps({'state': 9, 'message': 'params exit'}))
        except Exception as ex:
            LOG.error("Wx action %s error:%s" % (action, ex))
            self.finish(json.dumps({'state': 10, 'message': 'wx action error'}))

    def login(self):
        code = self.get_argument('code', '')
        user_name = self.get_argument('user_name', '')
        recommend_id = self.get_argument('recommend_id', '')

        app_id = relative_dic_con.get("appid")
        secret = relative_dic_con.get("secret")

        #微信服务器验证
        url = "https://api.weixin.qq.com/sns/jscode2session"
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
        session_key = dic_body.get('sessutilion_key')

        #存储openid和session_key,并返回识别session串
        #openid code session_key user_name recommend_id
        _op = WXUserLogic()
        exit_app = _op.info_by_openid(openid=openid)
        if exit_app:
            _op.update(exit_app.get("id"), session_key=session_key)
            self.finish(json.dumps({'state': 0, 'session_code': exit_app.get("id"), 'phone': exit_app.get("phone","")}))
        else:
            _ = _op.input(code=code,
                          openid=openid,
                          session_key=session_key,
                          user_name=user_name,
                          recommend_id=recommend_id)
            self.finish(json.dumps({'state': 0, 'session_code': _.get("id")}))
