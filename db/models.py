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

################################恐龙弹弹弹 begin###################################################################
class UserInfo(Base, ModelBase):
    __tablename__ = 'user_info'
    id = Column(VARCHAR(36), primary_key=True)
    user_name = Column(VARCHAR(50))
    recommend_id = Column(VARCHAR(36))
    property_glod = Column(Float, default=0)
    property_diamond = Column(Float, default=0)
    stance_items = Column(VARCHAR(3000), nullable=False)
    base_items = Column(VARCHAR(3000), nullable=False)
    book_ids = Column(VARCHAR(1000), nullable=False)
    buy_nums = Column(VARCHAR(2000), nullable=False)
    skill_items = Column(VARCHAR(1000), nullable=False)
    platform = Column(VARCHAR(100), nullable="wx")#默认微信服务平台
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class WxUserinfo(Base, ModelBase):
    __tablename__ = 'wx_userinfo'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36), nullable=False)
    openid = Column(VARCHAR(50) , nullable=False)
    code = Column(VARCHAR(36), nullable=False)
    session_key = Column(VARCHAR(50), nullable=False)
    wx_name = Column(VARCHAR(50))
    recommend_id = Column(VARCHAR(36))
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class SignIn(Base, ModelBase):
    __tablename__ = 'signin'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36))
    continuous = Column(Integer, default=0)
    lastdate = Column(Date, nullable=False)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)


class Share(Base, ModelBase):
    __tablename__ = 'share'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36))
    share_num = Column(Integer, default=0)
    lastdate = Column(Date, nullable=False)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class Advertising(Base, ModelBase):
    __tablename__ = 'advertising'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36))
    advertising_num = Column(Integer, default=0)
    lastdate = Column(Date, nullable=False)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class Welfare(Base, ModelBase):
    __tablename__ = 'welfare'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36))
    welfare_num = Column(Integer, default=0)
    lastdate = Column(Date, nullable=False)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class Chapter(Base, ModelBase):
    __tablename__ = 'chapter'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36))
    chapter_num = Column(Integer, default=0)
    not_pass = Column(VARCHAR(20), default="")
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class ChapterInfo(Base, ModelBase):
    __tablename__ = 'chapter_info'
    id = Column(VARCHAR(36), primary_key=True)
    chapter_index = Column(Integer, default=0)
    boss = Column(VARCHAR(200))
    ball_num = Column(Integer, default=0)
    barrier_indexs = Column(VARCHAR(200))
    barrier_nums = Column(VARCHAR(200))
    barrier_types = Column(VARCHAR(200))
    barrier_offset = Column(VARCHAR(200))
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class ChapterDiy(Base, ModelBase):
    __tablename__ = 'chapter_diy'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36))
    activate = Column(Boolean, default=False)
    boss = Column(VARCHAR(200))
    ball_num = Column(Integer, default=0)
    barrier_indexs = Column(VARCHAR(200))
    barrier_nums = Column(VARCHAR(200))
    barrier_types = Column(VARCHAR(200))
    barrier_offset = Column(VARCHAR(200))
    nick = Column(VARCHAR(50))
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class MaxScore(Base, ModelBase):
    __tablename__ = 'max_score'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36))
    score = Column(Integer, default=0)
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

################################恐龙弹弹弹 end###################################################################

################################鸡腿大作战 begin#################################################################
class DrumstickUserInfo(Base, ModelBase):
    __tablename__ = 'drumstick_userinfo'
    id = Column(VARCHAR(36), primary_key=True)
    user_name = Column(VARCHAR(50))
    avatar_url = Column(VARCHAR(150))
    recommend_id = Column(VARCHAR(36))
    glod = Column(Float, default=0)
    diamond = Column(Integer, default=0)
    hero_items = Column(VARCHAR(2000), nullable=False)
    map_items = Column(VARCHAR(500), nullable=False)
    prop_items = Column(VARCHAR(500), nullable=False)
    current_hero_id = Column(VARCHAR(10))
    current_map_id = Column(VARCHAR(10))
    kill_enemy = Column(Float, default=0) #杀敌数
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class DrumstickWxUserinfo(Base, ModelBase):
    __tablename__ = 'drumstick_wx_userinfo'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36), nullable=False)
    openid = Column(VARCHAR(50) , nullable=False)
    code = Column(VARCHAR(36), nullable=False)
    session_key = Column(VARCHAR(50), nullable=False)
    wx_name = Column(VARCHAR(50))
    recommend_id = Column(VARCHAR(36))
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)

class DrumstickAd(Base, ModelBase):
    __tablename__ = 'drumstick_ad'
    id = Column(VARCHAR(36), primary_key=True)
    user_id = Column(VARCHAR(36))
    advertising_num = Column(Integer, default=0)
    lastdate = Column(Date, nullable=False)
    deleted = Column(Boolean, default=False)

    def to_dict(self):
        return _to_dict(self)
################################鸡腿大作战 end###################################################################

def register_db():
    engine = get_engine()
    Base.metadata.create_all(engine)


def unregister_db():
    engine = get_engine()
    Base.metadata.drop_all(engine)