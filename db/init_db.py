# coding:utf-8

from db.models import register_db
from db import api

def add_monster(monster_data):
    try:
        for monster_info in monster_data:
            api.monster_create(monster_info)
        return True
    except Exception as ex:
        raise ex


if __name__ == "__main__":
    register_db()
    add_monster([])

