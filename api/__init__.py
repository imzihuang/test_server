#coding:utf-8

from tornado.web import StaticFileHandler
from api import wx_account, account
from api import drumstick
from settings import default_settings

def _handlers():
    prefix = default_settings.get('api_prefix', 'game')
    if prefix[-1] != '/':
        prefix += '/'
    return [
        (r'/wx_user/login$', wx_account.LoginHandler, default_settings),
        (r'/wx_user/storage$', wx_account.StorageHandler),
        (r'/game/user$', account.UserHandler),
        (r'/game/share$', account.ShareHandler),
        (r'/game/signin$', account.SigninHandler),
        (r'/game/advertising$', account.AdvertisingHandler),
        (r'/game/welfare$', account.WelfareHandler),
        (r'/game/chapter$', account.ChapterHandler),
        (r'/game/chapter_info$', account.ChapterInfoHandler),
        (r'/game/chapter_diy$', account.ChapterDiyHandler),
        (r'/game/notice$', account.NoticeHandler, default_settings),
        (r'/game/max_score$', account.MaxScoreHandler),

        (r'/drumstick/wx_user/login$', drumstick.DrumstickWxLoginHandler, default_settings),
        (r'/drumstick/game/user$', drumstick.DrumstickUserHandler, default_settings),
        (r'/drumstick/game/recommend$', drumstick.DrumstickRecommendHandler),
        (r'/drumstick/game/ad$', drumstick.DrumstickAdHandler, default_settings),
        (r'/drumstick/game/checkin$', drumstick.DrumstickCheckInHandler, default_settings),

        (prefix + r'(.*\.(css|png|js))', StaticFileHandler,
         {'path': default_settings.get('static_path')}),
        (r'(.*\.(css|png|js))', StaticFileHandler,
         {'path': default_settings.get('static_path')}),
    ]

api_handlers = _handlers()