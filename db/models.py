#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Table, MetaData, UniqueConstraint, ForeignKey

from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from base import get_engine, ModelBase

Base = declarative_base()

def _to_dict(model_obj):
    result = {}
    for c in model_obj.__table__.columns:
        if isinstance(getattr(model_obj, c.name, None), datetime):
            if c.name == "birthday":
                result.update({c.name: getattr(model_obj, c.name, None).strftime('%Y-%m-%d')})
            else:
                result.update({c.name: getattr(model_obj, c.name, None).strftime('%Y-%m-%d %H:%M:%S')})
        elif isinstance(getattr(model_obj, c.name, None), Base):
            result.update({c.name: getattr(model_obj, c.name, None).to_dict()})
        else:
            result.update({c.name: getattr(model_obj, c.name, None)})
    return result


class MonsterInfo(Base, ModelBase):
    __tablename__ = 'monster_info'
    id = Column(VARCHAR(36), primary_key=True)
    monster_name = Column(VARCHAR(36))
    resource = Column(VARCHAR(100))
    production = Column(VARCHAR(36), default="glod")
    production_base = Column(Integer, default=1)
    parent_id = Column(VARCHAR(36))
    price_glod = Column(Integer, default=1)
    price_diamond = Column(Integer, default=1)
    describe = Column(VARCHAR(200))
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class UserInfo(Base, ModelBase):
    __tablename__ = 'user_info'
    id = Column(VARCHAR(36), primary_key=True)
    openid = Column(VARCHAR(50), nullable=False)
    code = Column(VARCHAR(36), nullable=False)
    session_key = Column(VARCHAR(50), nullable=False)
    user_name = Column(VARCHAR(36), nullable=False)
    recommend_id = Column(VARCHAR(36))
    property_glod = Column(Integer, default=0)
    property_diamond = Column(Integer, default=0)
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class UserMonster(Base, ModelBase):
    __tablename__ = 'user_monster'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(50), ForeignKey("user_info.id"))
    monster_id = Column(VARCHAR(50), ForeignKey("monster_info.id"))
    stance_index = Column(Integer, default=0)
    level = Column(Integer, default=1)
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    user_info = relationship(UserInfo, backref='relation_list',
                                foreign_keys=user_id,
                                lazy='subquery',
                                primaryjoin='UserMonster.user_id == UserInfo.id')
    monster_info = relationship(MonsterInfo, backref='relation_list',
                             foreign_keys=user_id,
                             lazy='subquery',
                             primaryjoin='UserMonster.monster_id == MonsterInfo.id')

    def to_dict(self):
        return _to_dict(self)

def register_db():
    engine = get_engine()
    Base.metadata.create_all(engine)


def unregister_db():
    engine = get_engine()
    Base.metadata.drop_all(engine)