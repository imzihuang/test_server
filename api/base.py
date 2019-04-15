#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from util import common_util, convert
from logic.user import WXUserLogic
import logging
LOG = logging.getLogger(__name__)
def verify_token(func):
    """
    :param func:
    :return:
    """
    def __(torn_self):
        token = convert.bs2utf8(torn_self.get_argument('token', ''))
        user_id, dtime = common_util.dgen_token(token)
        #LOG.info("user id:"+user_id)
        #LOG.info(dtime)
        if dtime != 0 and int(time.time()) - dtime > 3600 * 5:  # 5小时内有效
            torn_self.finish({'state': 1, 'message': 'token error'})
            return
        user_op = WXUserLogic()
        user_info = user_op.info(user_id)
        if not user_info:
            torn_self.finish({'state': 8, 'message': 'token user error'})
            return
        func(torn_self, user_id)
    return __
