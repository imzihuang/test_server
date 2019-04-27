#coding:utf-8
import hmac
import hashlib
import base64

def get_sign(content, session_key):
    signature = hmac.new(bytes(session_key).encode('utf-8'), bytes(content).encode('utf-8'), digestmod=hashlib.sha256).digest()
    #signature = hmac.new(session_key, content, digestmod=hashlib.sha256).digest()
    return _toHex(signature)

def _toHex(str):
    lst = []
    for ch in str:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0' + hv
        lst.append(hv)
    return reduce(lambda x, y: x + y, lst)

print get_sign('{"foo":"bar"}', 'o0q0otL8aEzpcZL/FT9WsQ==')

