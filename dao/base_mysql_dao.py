# -*- coding: UTF-8 -*-
import pymysql

class base_mysql_dao(object):
    def __init__(self, host='127.0.0.1', port=3066, user='root', passwd='root', db='test', charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset

    def db_query(self, sql):
        '''
        查询数据库
        :param sql:
        :return:
        '''
        rs = []
        db = pymysql.connect(self.host,
                             self.port,
                             self.user,
                             self.passwd,
                             self.db, self.charset)
        try:
            cur = db.cursor()
            cur.execute(sql)
            rs = cur.fetchall()
            cur.close()
            db.commit()
            db.close()
        except Exception as e:
            print(e.message)
        return rs

    def db_modify(self, sql):
        '''
        更改数据库
        :param sql:
        :return:
        '''
        db = pymysql.connect(self.host,
                             self.port,
                             self.user,
                             self.passwd,
                             self.db, self.charset)
        try:
            cur = db.cursor()
            cur.execute(sql)
            cur.close()
            db.commit()
            db.close()
        except Exception as e:
            print(e.message)