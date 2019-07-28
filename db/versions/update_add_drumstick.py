# coding:utf-8
from sqlalchemy import Integer, MetaData, String, Table, Text, UniqueConstraint, DateTime
from base import get_engine

def define_tables(meta):
    drumstick_userinfo = Table(
        'drumstick_userinfo', meta,
        Column('id', VARCHAR(36), primary_key=True),
        Column('user_name', VARCHAR(50)),
        Column('recommend_id', VARCHAR(36)),
        Column('glod', Integer, default=0),
        Column('diamond', Integer, default=0),
        Column('hero_items', VARCHAR(2000), nullable=False),
        Column('map_items', VARCHAR(500), nullable=False),
        Column('current_hero_id', VARCHAR(10), defult="h001"),
        Column('create_time', DateTime, default=datetime.now, nullable=False),
        Column('updated_time', DateTime, default=datetime.now, onupdate=datetime.now),
        Column('deleted', Boolean, default=False),
        mysql_engine='InnoDB',
        mysql_charset='utf8',
    )

    drumstick_wx_userinfo = Table(
        'drumstick_wx_userinfo', meta,
        Column('id', VARCHAR(36), primary_key=True),
        Column('user_id', VARCHAR(36), nullable=False),
        Column('openid', VARCHAR(50), nullable=False),
        Column('code', VARCHAR(36), nullable=False),
        Column('session_key', VARCHAR(50), nullable=False),
        Column('wx_name', VARCHAR(50)),
        Column('recommend_id', VARCHAR(36)),
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