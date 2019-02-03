#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import or_, and_
from db import models
from db.base import *
from util import exception
from util import common_util


def model_query(model, session=None, order=False, read_deleted="no", desc=True, *args, **kwargs):
    """
    :param model:
    :param session: if present, the session to use
    """
    session = session or get_session()
    query = session.query(model, *args)

    if read_deleted == "no":
        query = query.filter_by(deleted=False)

    filter_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, tuple, set, frozenset)):
            column_attr = getattr(model, key)
            query = query.filter(column_attr.in_(value))
        else:
            filter_dict[key] = value

    if filter_dict:
        query = query.filter_by(**filter_dict)
    if order:
        if desc:
            query = query.order_by(model.create_time.desc())
        else:
            query = query.order_by(model.create_time)

    return query

#####################wx user begin################################
def wxuser_create(values):
    if not values.get('id'):
        values['id'] = common_util.create_id()
    wxuser_ref = models.UserInfo()
    wxuser_ref.update(values)
    session = get_session()
    with session.begin():
        wxuser_ref.save(session)
        return values

def wxuser_update(id, values):
    query = model_query(models.UserInfo).filter_by(id=id)
    result = query.update(values)
    if not result:
        return None
    return result

def wxuser_get(id):
    query = model_query(models.UserInfo)
    result = query.filter_by(id=id).first()
    if not result:
        return None
    return result

def wxuser_list(offset=0, limit=1000, **filters):
    query = model_query(models.UserInfo, order=True, **filters)
    if offset:
        query = query.offset(offset)
    if limit:
        query = query.limit(limit)
    return query.all()

def wxuser_count(**filters):
    query = model_query(models.UserInfo, **filters)
    return query.count()

def wxuser_deleted(id):
    session = get_session()
    with session.begin():
        query = model_query(models.UserInfo, session=session, id=id)
        query.update({
            "deleted": True
        },
        synchronize_session=False)

#####################wx user end################################

#####################monster begin################################
def monster_create(values):
    if not values.get('id'):
        values['id'] = common_util.create_id()
    wxuser_ref = models.MonsterInfo()
    wxuser_ref.update(values)
    session = get_session()
    with session.begin():
        wxuser_ref.save(session)
        return values

def monster_update(id, values):
    query = model_query(models.MonsterInfo).filter_by(id=id)
    result = query.update(values)
    if not result:
        return None
    return result

def monster_get(id):
    query = model_query(models.MonsterInfo)
    result = query.filter_by(id=id).first()
    if not result:
        return None
    return result

def monster_list(offset=0, limit=1000, **filters):
    query = model_query(models.MonsterInfo, order=True, **filters)
    if offset:
        query = query.offset(offset)
    if limit:
        query = query.limit(limit)
    return query.all()

def monster_count(**filters):
    query = model_query(models.MonsterInfo, **filters)
    return query.count()

def monster_deleted(id):
    session = get_session()
    with session.begin():
        query = model_query(models.MonsterInfo, session=session, id=id)
        query.update({
            "deleted": True
        },
        synchronize_session=False)

#####################monster end################################

##################### user monster begin################################
def usermonster_create(values):
    if not values.get('id'):
        values['id'] = common_util.create_id()
    wxuser_ref = models.UserMonster()
    wxuser_ref.update(values)
    session = get_session()
    with session.begin():
        wxuser_ref.save(session)
        return values

def usermonster_update(id, values):
    query = model_query(models.UserMonster).filter_by(id=id)
    result = query.update(values)
    if not result:
        return None
    return result

def usermonster_get(id):
    query = model_query(models.UserMonster)
    result = query.filter_by(id=id).first()
    if not result:
        return None
    return result

def usermonster_list(offset=0, limit=1000, **filters):
    query = model_query(models.UserMonster, order=True, **filters)
    if offset:
        query = query.offset(offset)
    if limit:
        query = query.limit(limit)
    return query.all()

def usermonster_count(**filters):
    query = model_query(models.UserMonster, **filters)
    return query.count()

def usermonster_deleted(id):
    session = get_session()
    with session.begin():
        query = model_query(models.UserMonster, session=session, id=id)
        query.update({
            "deleted": True
        },
        synchronize_session=False)

##################### user monster end################################