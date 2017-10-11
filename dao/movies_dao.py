# -*- coding: UTF-8 -*-
from . import base_mongodb_dao

db = base_mongodb_dao

def insert_moveis(data):
    db.insert(data)

