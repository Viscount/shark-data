#!/usr/bin/python
# -*- coding: utf-8 -*-

from entity.user import User
import datetime
from connection.connector_singleton import *


def get_users(start_date=datetime.date(2016, 1, 1), end_date=datetime.date.today()):
    model = MysqlConnModel.get_instance()
    user_list = model.find("user", {"createdAt": {"$gt": start_date, "$lt": end_date}}, multi=True)
    user_obj_list = []
    for user_record in user_list:
        user_obj = User(user_record)
        user_obj_list.append(user_obj)
    return user_obj_list


def get_user_by_id(id):
    model = MysqlConnModel.get_instance()
    user = model.find("user", {"id": id}, multi=False)
    if len(user) < 1:
        return None
    else:
        return User(user[0])


def get_users_by_ids(id_list):
    model = MysqlConnModel.get_instance()
    user_list = model.find("user", {"id": id_list}, multi=True)
    user_obj_list = []
    for user_record in user_list:
        user_obj = User(user_record)
        user_obj_list.append(user_obj)
    return user_obj_list


if __name__ == "__main__":
    print len(get_users())
