#!/usr/bin/python
# -*- coding: utf-8 -*-

import connection.mysql
import datetime
from connection.model import MySQLModel
from entity.clazz_account import ClazzAccount


def get_purchase_records(time_constraint=datetime.date(2016, 1, 1)):
    mysql_mc = connection.mysql.MySQLConnector()
    mysql_mm = MySQLModel(mysql_mc)
    clazz_account_list = mysql_mm.find("clazz_account", {"status": ["PROCESSING", "WAITENTER", "CLOSE"],
                                                         "joinDate": {"$gt": time_constraint}}, multi=True)
    clazz_account_object_list = []
    for record in clazz_account_list:
        clazz_account = ClazzAccount(record)
        clazz_account_object_list.append(clazz_account)
    return clazz_account_object_list


if __name__ == "__main__":
    print len(get_purchase_records())
