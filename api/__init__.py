#coding:utf-8

from tornado.web import StaticFileHandler
from api import wx_account, account
from settings import default_settings

def _handlers():
    prefix = default_settings.get('api_prefix', 'game')
    if prefix[-1] != '/':
        prefix += '/'
    return [
        (r'/wx_user/login$', wx_account.LoginHandler, default_settings),
        (r'/wx_user/storage$', wx_account.StorageHandler),
        (r'/game/user', account.UserHandler),
        (r'/game/share', account.ShareHandler),
        (r'/game/signin', account.SigninHandler),
        (r'/game/advertising', account.AdvertisingHandler),

        (prefix + r'(.*\.(css|png|js))', StaticFileHandler,
         {'path': default_settings.get('static_path')}),
    ]

api_handlers = _handlers()