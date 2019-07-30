#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Index
from sqlalchemy import Integer, MetaData, String, Table, Text, UniqueConstraint
from test_server.db.base import *

def define_tables(meta):
    drumstick_userinfo = Table(
        'drumstick_userinfo', meta,
        Column('id', String(36), primary_key=True),
        Column('user_name', String(50)),
        Column('avatarUrl', String(150)),
        Column('recommend_id', String(36)),
        Column('glod', Integer, default=0),
        Column('diamond', Integer, default=0),
        Column('hero_items', String(2000), nullable=False),
        Column('map_items', String(500), nullable=False),
        Column('current_hero_id', String(10)),
        Column('create_time', DateTime, default=datetime.now, nullable=False),
        Column('updated_time', DateTime, default=datetime.now, onupdate=datetime.now),
        Column('deleted', Boolean, default=False),
        mysql_engine='InnoDB',
        mysql_charset='utf8',
    )

    drumstick_wx_userinfo = Table(
        'drumstick_wx_userinfo', meta,
        Column('id', String(36), primary_key=True),
        Column('user_id', String(36), nullable=False),
        Column('openid', String(50), nullable=False),
        Column('code', String(36), nullable=False),
        Column('session_key', String(50), nullable=False),
        Column('wx_name', String(50)),
        Column('recommend_id', String(36)),
        Column('create_time', DateTime, default=datetime.now, nullable=False),
        Column('updated_time', DateTime, default=datetime.now, onupdate=datetime.now),
        Column('deleted', Boolean, default=False),
        mysql_engine = 'InnoDB',
        mysql_charset = 'utf8'
    )

    return [drumstick_userinfo,
            drumstick_wx_userinfo]

if __name__ == "__main__":
    engine = get_engine()
    meta = MetaData()
    meta.bind = engine
    tables = define_tables(meta)

    for table in tables:
        table.create()