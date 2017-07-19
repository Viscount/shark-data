#!/usr/bin/python
# -*- coding: utf-8 -*-

from entity.user import User
from connection.connector_singleton import *


def get_users():
    model = MysqlConnModel.get_instance()
    user_list = model.find("user", {}, multi=True)
    user_obj_list = []
    for user_record in user_list:
        user_obj = User(user_record)
        user_obj_list.append(user_obj)
    return user_obj_list


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
