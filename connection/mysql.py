#!/usr/bin/python
# -*- coding: utf-8 -*-

import config
import pymysql


class MySQLConnector:
    _conn = pymysql.connect(**config.MYSQL)
    _cursor = _conn.cursor()

    def __init__(self):
        MySQLConnector._cursor.execute('SET NAMES utf8mb4')
        MySQLConnector._cursor.execute("SET CHARACTER SET utf8mb4")
        MySQLConnector._cursor.execute("SET character_set_connection=utf8mb4")

    @staticmethod
    def getConnect():
        return MySQLConnector._conn
    
    @staticmethod
    def getCursor():
        return MySQLConnector._cursor
    
    @staticmethod
    def execute(sql):
        # print '>>>', sql
        try:
            MySQLConnector._cursor.execute(sql)
            MySQLConnector._conn.commit()
        except:
            print 'ERROR: Execute failure.'
            MySQLConnector._conn.rollback()
        try:
            results = MySQLConnector._cursor.fetchall()
        except:
            results = None
        return results
    
    def getTables(self):
        res = self.execute('show tables;')
        return [str(x[0]) for x in res]

    def getRows(self, table):
        res = self.execute('desc %s;' % table)
        return [str(x[0]) for x in res]

    def getStruct(self):
        t = self.getTables()
        print t
        for i in t:
            print self.getRows(i)

    
if __name__ == '__main__':
    mc = MySQLConnector()
    mc.getStruct()
