#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import *
from pytz import reference
from service import clazz_service, user_service, purchase_service
from util import export_service


# 班级数
# 返回值：平台开设班级的数量
# 返回类型：int
def clazz_count():
    return len(clazz_service.get_all_clazz())


# 班级内新用户名单
# 返回值：用户信息列表
# 返回类型：list(User类)
def new_student_for_clazz(clazz_id):
    user_list = clazz_service.get_clazz_users_id(clazz_id)
    purchase_records = purchase_service.get_purchase_records_for_users(user_list)
    # 建立字典统计购买次数
    purchase_times_dict = dict()
    for purchase_record in purchase_records:
        if str(purchase_record.userId) in purchase_times_dict:
            purchase_times_dict[str(purchase_record.userId)] += 1
        else:
            purchase_times_dict[str(purchase_record.userId)] = 1
    # 找出只购买一次的
    new_student_name_list = []
    for user in user_list:
        if purchase_times_dict[str(user)] == 1:
            new_student_name_list.append(user)
    return user_service.get_users_by_ids(new_student_name_list)


# 一段时间内打卡次数不足用户名单
# 参数：课程ID，统计开始时间，统计结束时间，最低次数要求
# 参数类型：string, datetime. datetime, int
# 返回值：用户信息列表
# 返回类型：list(User类)
def uncheck_clazz_users(clazz_id, start_date, end_date, limit):
    user_id_list = clazz_service.get_clazz_users_id(clazz_id)
    checkin_list = clazz_service.get_clazz_checkin(clazz_id, start_date, end_date)
    user_check_time = dict()
    for checkin in checkin_list:
        if checkin.userId in user_check_time:
            user_check_time[checkin.userId] += 1
        else:
            user_check_time[checkin.userId] = 1
    uncheck_user_ids = []
    for user_id in user_id_list:
        if user_id in user_check_time:
            if user_check_time[user_id] < limit:
                uncheck_user_ids.append(user_id)
        else:
            uncheck_user_ids.append(user_id)
    user_info_list = user_service.get_users_by_ids(uncheck_user_ids)
    return user_info_list


if __name__ == "__main__":
    # print clazz_count()
    # 统计上周、本周各班打卡次数不合格者，并且统计了改善的人
    clazz_object = clazz_service.get_clazz_by_name("听力训练班8月")
    start_date = datetime(datetime.today().year,
                          datetime.today().month,
                          datetime.today().day,
                          tzinfo=reference.LocalTimezone()) - timedelta(days=9)
    end_date = datetime(datetime.today().year,
                        datetime.today().month,
                        datetime.today().day,
                        tzinfo=reference.LocalTimezone()) - timedelta(days=2)
    name_list = uncheck_clazz_users(clazz_object.id, start_date, end_date, 4)

    print start_date
    print end_date

    content_list = []
    for user in name_list:
        content_list.append(user.csv_format())
    export_service.export2csv('this_week.csv', content_list)

    # last_week_start_date = datetime(datetime.today().year,
    #                        datetime.today().month,
    #                        datetime.today().day,
    #                        tzinfo=reference.LocalTimezone()) - timedelta(days=12)
    # name_list_last_week = uncheck_clazz_users(clazz_object.id, last_week_start_date, start_date, 4)
    #
    # content_list = []
    # for user in name_list_last_week:
    #     content_list.append(user.csv_format())
    # export_service.export2csv('last_week.csv', content_list)
    #
    # print last_week_start_date
    #
    # improved_user = []
    # content_list = []
    # for user in name_list_last_week:
    #     flag = False
    #     for com_user in name_list:
    #         if com_user.id == user.id:
    #             flag = True
    #             break
    #     if not flag:
    #         improved_user.append(user)
    #         content_list.append(user.csv_format())
    # export_service.export2csv('improved.csv', content_list)

    # 输出班级新成员名单
    # clazz_object = clazz_service.get_clazz_by_name("法语基础班-S1")
    # user_list = new_student_for_clazz(clazz_object.id)
    # contents = []
    # for user in user_list:
    #     contents.append(user.csv_format())
    # export_service.export2csv("new_students.csv", contents)

    # 输出班级打卡情况
    # clazz_object = clazz_service.get_clazz_by_name("语法训练班")
    # export_service.export2csv('grammar_class.csv', [clazz_object.csv_format()])
    # user_id_list = clazz_service.get_clazz_users(clazz_object.id)
    # user_obj_list = user_service.get_users_by_ids(user_id_list)
    # content_list = []
    # for user in user_obj_list:
    #     content_list.append(user.csv_format(privacy=True))
    # export_service.export2csv('grammar_class_users.csv', content_list)
    # checkin_list = clazz_service.get_clazz_checkin(clazz_object.id, clazz_object.start_date, clazz_object.end_date)
    # content_list = []
    # for checkin in checkin_list:
    #     content_list.append(checkin.csv_format())
    # export_service.export2csv('grammar_class_checkins.csv', content_list)



