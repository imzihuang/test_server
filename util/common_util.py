# coding=utf-8

import uuid
from random import randint



def create_id():
    return uuid.uuid4().get_hex()

def create_verifycode():
    """
    生成注册验证码
    :return:
    """
    verify_code = ''.join((str(randint(0, 9)) for _ in range(6)))
    return verify_code