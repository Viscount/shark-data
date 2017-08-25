#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from connection.connector_singleton import *
from entity.clazz_account import ClazzAccount


def get_purchase_records(time_constraint=datetime.date(2016, 1, 1)):
    model = MysqlConnModel.get_instance()
    clazz_account_list = model.find("clazz_account", {"status": ["PROCESSING", "WAITENTER", "CLOSE"],
                                                         "joinDate": {"$gt": time_constraint}}, multi=True)
    clazz_account_object_list = []
    for record in clazz_account_list:
        clazz_account = ClazzAccount(record)
        clazz_account_object_list.append(clazz_account)
    return clazz_account_object_list


def get_purchase_records_for_clazz(clazz_id):
    model = MysqlConnModel.get_instance()
    clazz_account_list = model.find("clazz_account", {"status": ["PROCESSING", "WAITENTER", "CLOSE"],
                                                         "clazzId": clazz_id}, multi=True)
    clazz_account_object_list = []
    for record in clazz_account_list:
        clazz_account = ClazzAccount(record)
        clazz_account_object_list.append(clazz_account)
    return clazz_account_object_list


def get_purchase_records_for_users(user_id_list):
    model = MysqlConnModel.get_instance()
    clazz_account_list = model.find("clazz_account", {"status": ["PROCESSING", "WAITENTER", "CLOSE"],
                                                         "userId": user_id_list}, multi=True)
    clazz_account_object_list = []
    for record in clazz_account_list:
        clazz_account = ClazzAccount(record)
        clazz_account_object_list.append(clazz_account)
    return clazz_account_object_list


if __name__ == "__main__":
    print len(get_purchase_records(time_constraint=datetime.date(2017, 7, 1)))
