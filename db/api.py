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

def wxuser_get_session_key(session_key):
    query = model_query(models.UserInfo)
    result = query.filter_by(session_key=session_key).first()
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

#####################wx user end##################################

#####################wx user signin begin################################
def signin_create(values):
    if not values.get('id'):
        values['id'] = common_util.create_id()
    signin_ref = models.SignIn()
    signin_ref.update(values)
    session = get_session()
    with session.begin():
        signin_ref.save(session)
        return values

def signin_update(id, values):
    query = model_query(models.SignIn).filter_by(id=id)
    result = query.update(values)
    if not result:
        return None
    return result

def signin_get_userid(user_id):
    query = model_query(models.SignIn)
    result = query.filter_by(user_id=user_id).first()
    if not result:
        return None
    return result

def signin_list(offset=0, limit=1000, **filters):
    query = model_query(models.SignIn, order=True, **filters)
    if offset:
        query = query.offset(offset)
    if limit:
        query = query.limit(limit)
    return query.all()

def signin_count(**filters):
    query = model_query(models.SignIn, **filters)
    return query.count()
#####################wx user signin end################################