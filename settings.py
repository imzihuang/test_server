#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
import logging

STATIC_PATH = os.path.join(os.path.dirname(os.path.normpath(__file__)), 'static')
TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.normpath(__file__)), 'templates')

default_settings = {
    'base_url': '/',
    'view_prefix': '/game',
    'static_path': STATIC_PATH,
    'templates_path': TEMPLATES_PATH,
    'api_version': 'v1.0',
    'enabled_methods': ['get', 'post', 'put', 'patch', 'delete'],
    'exclude_namespaces': [],
    'log_info': "./log/game_info.log",
    'log_error': "./log/game_error.log",
    'excel_path': '/excel/tmp',
    'book_ids': ["0101"],
    'stance_items': [{"m_id": "0101", 'lvl':1, "index":1}],
    'buy_nums':[],#[{"id":"0101", "g":1, "d":1}] 购买一次
    'skill_items':[],#技能位[{"m_id": "0101", 'lvl':1, "index":1}]
    'version': "1.0",
    'content': "新增弹珠营救模式，大家一起去营救可爱的恐龙宝宝吧~~",
}

models = []

Debug = False

if Debug:
    logging.basicConfig(level=logging.DEBUG)
