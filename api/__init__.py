#coding:utf-8

from tornado.web import StaticFileHandler
from api import infos, wx_action
from settings import default_settings

def _handlers():
    prefix = default_settings.get('api_prefix', 'game')
    if prefix[-1] != '/':
        prefix += '/'
    return [
        (r'/(?P<infos_obj>.+)/infos$', infos.InfosHandler),
        (r'/(?P<action>.+)/wx_action$', wx_action.WXActionHandler, default_settings),
        (prefix + r'(.*\.(css|png|js))', StaticFileHandler,
         {'path': default_settings.get('static_path')}),
    ]

api_handlers = _handlers()