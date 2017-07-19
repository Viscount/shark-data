#!/usr/bin/python
# -*- coding: utf-8 -*-

from pytz import reference
from datetime import *
from connection.connector_singleton import *
from entity.clazz_account import ClazzAccount
from entity.checkin import Checkin
from entity.clazz import Clazz


def get_clazz_count():
    model = MongoConnModel.get_instance()
    clazz_list = model.find('Clazz', {}, multi=True)
    clazz_obj_list = []
    for clazz_record in clazz_list:
        clazz_obj = Clazz(clazz_record)
        clazz_obj_list.append(clazz_obj)
    return clazz_obj_list


def get_active_clazz():
    model = MongoConnModel.get_instance()
    clazz_list = model.find('Clazz', {'status': 'PROCESSING'}, multi=True)
    clazz_obj_list = []
    for clazz_record in clazz_list:
        clazz_obj = Clazz(clazz_record)
        clazz_obj_list.append(clazz_obj)
    return clazz_obj_list


def get_clazz_users(clazz_id):
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
    clazz_list = get_active_clazz()
    print clazz_list[14].name
    start_date = datetime(datetime.today().year,
                          datetime.today().month,
                          datetime.today().day,
                          tzinfo=reference.LocalTimezone())-timedelta(days=1)
    end_date = datetime(datetime.today().year,
                        datetime.today().month,
                        datetime.today().day,
                        tzinfo=reference.LocalTimezone())
    print start_date
    print end_date
    print len(get_clazz_checkin(clazz_list[14].id, start_date, end_date))
