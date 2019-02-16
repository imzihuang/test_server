#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
import logging

STATIC_PATH = os.path.join(os.path.dirname(os.path.normpath(__file__)), 'static')
TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.normpath(__file__)), 'templates')

default_settings = {
    'base_url': '/',
    'view_prefix': '/edu',
    'static_path': STATIC_PATH,
    'templates_path': TEMPLATES_PATH,
    'api_version': 'v1.0',
    'enabled_methods': ['get', 'post', 'put', 'patch', 'delete'],
    'exclude_namespaces': [],
    'log_info': "./log/edu_info.log",
    'log_error': "./log/edu_error.log",
    'excel_path': '/excel/tmp',
    'book_ids': ["0101","0102","0103","0104","0201","0202","0203","0204"],
    'stance_items': {"1":{"m_id": "0101", 'lvl':1}}
}

models = []

Debug = False

if Debug:
    logging.basicConfig(level=logging.DEBUG)
