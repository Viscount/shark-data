#!/usr/bin/python
# -*- coding: utf-8 -*-

import mongo
import mysql
from model import MongoModel, MySQLModel


class MongoConnModel():
    __instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if MongoConnModel.__instance is None:
            mongo_mc = mongo.MongoConnector()
            mongo_mm = MongoModel(mongo_mc)
            MongoConnModel.__instance = mongo_mm
        return MongoConnModel.__instance


class MysqlConnModel():
    __instance = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if MysqlConnModel.__instance is None:
            mysql_mc = mysql.MySQLConnector()
            mysql_mm = MySQLModel(mysql_mc)
            MysqlConnModel.__instance = mysql_mm
        return MysqlConnModel.__instance
