#!/usr/bin/python
# -*- coding: utf-8 -*-
from db.example import Base
from db import models

class UserDB(Base):
    def __init__(self):
        self.model = models.UserInfo