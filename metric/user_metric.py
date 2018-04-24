#!/usr/bin/python
# -*- coding: utf-8 -*-

from service import purchase_service, user_service, clazz_service
from util import export_service, date_service
import datetime
import json


# 付费用户数
# 返回值：平台中至少参与了一个班级的用户数量
# 返回类型：int
def paid_user_count():
    record_list = purchase_service.get_purchase_records()
    user_set = set()
    for record in record_list:
        user_set.add(record.userId)
    return len(user_set)


# 付费用户数，按月统计
# 参数：统计开始时间
# 参数类型：string，满足日期格式"%Y-%m-%d"
# 返回值：月份与付费用户数对应字典
# 返回类型：dict（月份：用户数）
def paid_user_count_series(start_date="2016-07-01"):
    timeline = date_service.get_between_month(start_date)
    paid_user_count_dict = dict()
    for month in timeline:
        record_list = purchase_service.get_purchase_records(end_date=month.start_date)
        user_set = set()
        for record in record_list:
            user_set.add(record.userId)
        paid_user_count_dict[month.name] = len(user_set)
    return paid_user_count_dict


# 关注用户数
# 返回值：曾经关注公众号的用户数量
# 返回类型：int
def subscribe_user_count():
    user_list = user_service.get_users()
    return len(user_list)


# 关注用户数，按月统计
# 参数：统计开始时间
# 参数类型：string，满足日期格式"%Y-%m-%d"
# 返回值：月份与关注用户数对应字典
# 返回类型：dict（月份：用户数）
def subscribe_user_count_series(start_date="2016-07-01"):
    timeline = date_service.get_between_month(start_date)
    sub_user_count_dict = dict()
    for month in timeline:
        user_list = user_service.get_users(end_date=month.start_date)
        sub_user_count_dict[month.name] = len(user_list)
    return sub_user_count_dict


# 购买指定课程数量的用户名单
# 参数：课程购买数量
# 参数类型：int
# 返回值：用户信息字典
# 返回类型：Dict(userId-list(clazzId))
def paid_user_dict_by_times(times):
    record_list = purchase_service.get_purchase_records()
    user_paid_times_count = dict()
    for paid_record in record_list:
        user_id = str(paid_record.userId)
        if user_id == 'None':
            continue
        if user_id in user_paid_times_count:
            user_paid_times_count[user_id].append(paid_record.clazzId)
        else:
            clazz_detail = [paid_record.clazzId]
            user_paid_times_count[user_id] = clazz_detail
    user_ids_dict = dict()
    for user_id in user_paid_times_count:
        if len(user_paid_times_count[user_id]) == times:
            user_ids_dict[user_id] = user_paid_times_count[user_id]
    return user_ids_dict


if __name__ == "__main__":
    # 关注用户数
    # print subscribe_user_count()

    # 付费用户数
    # print paid_user_count()

    # 输出购买指定次数的名单
    # user_clazz_id_dict = paid_user_dict_by_times(1)
    # user_ids_all = user_clazz_id_dict.keys()
    # clazz_ids_all = set()
    # for user_id in user_clazz_id_dict:
    #     clazz_id_list = user_clazz_id_dict[user_id]
    #     for clazz_id in clazz_id_list:
    #         clazz_ids_all.add(clazz_id)
    # user_obj_list = user_service.get_users_by_ids(list(user_ids_all))
    # clazz_obj_list = clazz_service.get_clazz_by_ids(list(clazz_ids_all))
    # user_lookup = dict()
    # for user in user_obj_list:
    #     user_lookup[str(user.id)] = user
    # clazz_lookup = dict()
    # for clazz in clazz_obj_list:
    #     clazz_lookup[str(clazz.id)] = clazz
    # content_list = []
    # for user_id in user_clazz_id_dict:
    #     if user_id not in user_lookup:
    #         continue
    #     content = user_lookup[user_id].csv_format()
    #     clazz_id_list = user_clazz_id_dict[str(user_id)]
    #     for clazz_id in clazz_id_list:
    #         content.append(clazz_lookup[clazz_id].name)
    #     content_list.append(content)
    # export_service.export2csv("1.csv", content_list)

    # 输出所有付费用户的购买记录
    # record_list = purchase_service.get_purchase_records()
    # user_buy_dict = dict()
    # for record in record_list:
    #     if str(record.userId) in user_buy_dict:
    #         pay_list = user_buy_dict[str(record.userId)]
    #         pay_list.append(record.clazzId)
    #         user_buy_dict[str(record.userId)] = pay_list
    #     else:
    #         user_buy_dict[str(record.userId)] = [record.clazzId]
    # content_list = []
    # for user_id in user_buy_dict:
    #     user_pay_list = user_buy_dict[user_id]
    #     clazz = "|".join(user_pay_list)
    #     content = [user_id, clazz]
    #     content_list.append(content)
    # export_service.export2csv("user_pay.csv", content_list)

    # 输出指定班级的购买记录
    # clazz_object = clazz_service.get_clazz_by_name("安妮的笔译训练班")
    # record_list = purchase_service.get_purchase_records_for_clazz(clazz_object.id)
    # user_ids = set(record.userId for record in record_list)
    # users = user_service.get_users_by_ids(list(user_ids))
    # content_list = []
    # for user in users:
    #     content_list.append(user.csv_format())
    # export_service.export2csv("user_pay.csv", content_list)

    # 输出所有用户信息
    # users = user_service.get_users()
    # content_list = []
    # for user in users:
    #     content_list.append(user.csv_format(privacy=True))
    # export_service.export2csv("users.csv", content_list)

    # 输出指定时间内关注的用户（未购买）
    # users_no_bought = user_service.get_users(start_date=datetime.date(2017, 9, 1))
    # records = purchase_service.get_purchase_records(start_date=datetime.date(2017, 9, 1))
    # user_bought = set()
    # for record in records:
    #     user_bought.add(record.userId)
    # for user in users_no_bought:
    #     if user.id in user_bought:
    #         users_no_bought.remove(user)
    # content_list = []
    # for user in users_no_bought:
    #     content_list.append(user.csv_format())
    # export_service.export2csv("users_no_bought.csv", content_list)

    # 输出指定时间内购买过的用户
    record_list = purchase_service.get_purchase_records(start_date=datetime.date(2017, 1, 1))
    user_buy_dict = dict()
    for record in record_list:
        if str(record.userId) in user_buy_dict:
            pay_list = user_buy_dict[str(record.userId)]
            pay_list.append(record.clazzId)
            user_buy_dict[str(record.userId)] = pay_list
        else:
            user_buy_dict[str(record.userId)] = [record.clazzId]
    content_list = []
    for user_id in user_buy_dict:
        user = user_service.get_user_by_id(user_id)
        if user is None:
            continue
        user_pay_list = user_buy_dict[user_id]
        clazz_infos = clazz_service.get_clazz_by_ids(user_pay_list)
        clazz = "|".join([clazz_info.name for clazz_info in clazz_infos])
        content = [user.id, user.name, user.student_number, clazz]
        content_list.append(content)
    export_service.export2csv("user_pay.csv", content_list)
