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


class UserInfo(Base, ModelBase):
    __tablename__ = 'user_info'
    id = Column(VARCHAR(36), primary_key=True)
    openid = Column(VARCHAR(50), nullable=False)
    code = Column(VARCHAR(36), nullable=False)
    session_key = Column(VARCHAR(50), nullable=False)
    user_name = Column(VARCHAR(36), nullable=False)
    recommend_id = Column(VARCHAR(36))
    property_glod = Column(Float, default=0)
    property_diamond = Column(Float, default=0)
    stance_items = Column(VARCHAR(3000), nullable=False)
    base_items = Column(VARCHAR(3000), nullable=False)
    book_ids = Column(VARCHAR(1000), nullable=False)
    buy_nums = Column(VARCHAR(1000), nullable=False)
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)


class SignIn(Base, ModelBase):
    __tablename__ = 'signin'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36), primary_key=True)
    continuous = Column(Integer, default=0)
    lastdate = Column(Date, nullable=False)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)


class Share(Base, ModelBase):
    __tablename__ = 'share'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36), primary_key=True)
    share_num = Column(Integer, default=0)
    lastdate = Column(Date, nullable=False)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

def register_db():
    engine = get_engine()
    Base.metadata.create_all(engine)


def unregister_db():
    engine = get_engine()
    Base.metadata.drop_all(engine)