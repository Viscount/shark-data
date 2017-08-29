#!/usr/bin/python
# -*- coding: utf-8 -*-

from pytz import reference
from datetime import *
from bson import ObjectId
from connection.connector_singleton import *
from entity.clazz_account import ClazzAccount
from entity.checkin import Checkin
from entity.clazz import Clazz


def get_all_clazz(time_constraint=datetime.now()):
    model = MongoConnModel.get_instance()
    clazz_list = model.find("Clazz", {"createdAt": {"$lte": time_constraint}}, multi=True)
    if clazz_list is None:
        return []
    clazz_obj_list = []
    for clazz_record in clazz_list:
        clazz_obj = Clazz(clazz_record)
        clazz_obj_list.append(clazz_obj)
    return clazz_obj_list


def get_active_clazz():
    model = MongoConnModel.get_instance()
    clazz_list = model.find("Clazz", {"status": 'PROCESSING'}, multi=True)
    if clazz_list is None:
        return []
    clazz_obj_list = []
    for clazz_record in clazz_list:
        clazz_obj = Clazz(clazz_record)
        clazz_obj_list.append(clazz_obj)
    return clazz_obj_list


def get_clazz_by_name(clazz_name):
    model = MongoConnModel.get_instance()
    clazz_result = model.find("Clazz", {"name": clazz_name}, multi=False)
    return Clazz(clazz_result)


def get_clazz_by_ids(clazz_id_list):
    clazz_objectId_list = []
    for clazz_id in clazz_id_list:
        if isinstance(clazz_id, ObjectId):
            clazz_objectId_list.append(clazz_id)
        else:
            clazz_objectId_list.append(ObjectId(clazz_id))
    model = MongoConnModel.get_instance()
    clazz_list = model.find("Clazz", {"_id": {"$in": clazz_objectId_list}}, multi=True)
    if clazz_list is None:
        return []
    clazz_obj_list = []
    for clazz_record in clazz_list:
        clazz_obj = Clazz(clazz_record)
        clazz_obj_list.append(clazz_obj)
    return clazz_obj_list


def get_clazz_users_id(clazz_id):
    model = MysqlConnModel.get_instance()
    clazz_account_list = model.find("clazz_account", {"status": ["PROCESSING", "WAITENTER", "CLOSE"],
                                                      "clazzId": clazz_id}, multi=True)
    clazz_users = []
    for record in clazz_account_list:
        clazz_account = ClazzAccount(record)
        clazz_users.append(clazz_account.userId)
    return clazz_users


def get_clazz_checkin(clazz_id, start_date, end_date):
    model = MongoConnModel.get_instance()
    checkin_list = model.find("Checkin", {"clazz": clazz_id,
                                          "status": "NORMAL",
                                          "checkinTime": {"$gte": start_date, "$lte": end_date}}, multi=True)
    checkin_obj_list = []
    for checkin_record in checkin_list:
        checkin_obj = Checkin(checkin_record)
        checkin_obj_list.append(checkin_obj)
    return checkin_obj_list


if __name__ == "__main__":
    list = get_active_clazz()
    clazz_list = get_clazz_by_ids([list[0].id, list[1].id])
    print len(clazz_list)
