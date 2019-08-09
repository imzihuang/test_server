#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import MetaData, Table, Column, Text, Float
from test_server.db.base import *


def upgrade(meta):
    # Add connection_info column to attachment table
    userinfo = Table('drumstick_userinfo', meta, autoload=True)
    kill_enemy = Column("kill_enemy", Float, default=0) #杀敌数
    if not hasattr(userinfo.c, 'kill_enemy'):
        userinfo.create_column(kill_enemy)


if __name__ == "__main__":
    engine = get_engine()
    meta = MetaData()
    meta.bind = engine

    upgrade(meta)