#!/usr/bin/python
# -*- coding: utf-8 -*-
from db.example import Base
from db import models
from db import api

class DrumstickCheckInDB(Base):
    def __init__(self):
        self.model = models.DrumstickCheckIn

    def info_userid(self, user_id):
        query = api.model_query(self.model)
        result = query.filter_by(user_id=user_id).first()
        if not result:
            return None
        return result