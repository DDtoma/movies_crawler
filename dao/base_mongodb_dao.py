# -*- coding: UTF-8 -*-
from pymongo import MongoClient
import config

config = config.config
client = MongoClient(config.mongodb_url)
db = client.movies_crawler
movies_db = db.movies

def  insert(data):
    movies_db.insert(data)

def insert_one(data):
    movies_db.insert_one(data)

def get_collections():
    return db.collection_names()

def find(conditions):
    if isinstance(conditions, dict):
        all = movies_db.find(conditions)
        l_result = []
        for one in all:
            l_result.append(one)
        return l_result
    else:
        print('conditions is not dict type')

def find_one(conditions):
    if isinstance(conditions, dict):
        one = movies_db.find_one(conditions)
        return one
    else:
        print('conditions is not dict type')


if __name__ == '__main__':
    data = {'name': 'llight', 'age': 19}
    datas = [{'name': 'TT', 'age': 19},{'name': 'CC', 'age': 100}]
