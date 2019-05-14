#!/usr/bin/python
# -*- coding: utf-8 -*-
from db.example import Base
from db import models, api

class ChapterInfoDB(Base):
    def __init__(self):
        self.model = models.ChapterInfo

    def info_by_index(self, index):
        query = api.model_query(self.model)
        result = query.filter_by(index=index).first()
        if not result:
            return None
        return result
