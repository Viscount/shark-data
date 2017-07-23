#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import *
from pytz import reference
from service import clazz_service, user_service
from util import export_service


# 班级数
# 返回值：平台开设班级的数量
# 返回类型：int
def clazz_count():
    return len(clazz_service.get_all_clazz())


# 一段时间内打卡次数不足用户名单
# 参数：课程ID，统计开始时间，统计结束时间，最低次数要求
# 参数类型：string, datetime. datetime, int
# 返回值：用户信息列表
# 返回类型：list(User类)
def uncheck_clazz_users(clazz_id, start_date, end_date, limit):
    user_id_list = clazz_service.get_clazz_users(clazz_id)
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
    print clazz_count()
    # clazz_list = clazz_service.get_active_clazz()
    # print clazz_list[8].name
    # start_date = datetime(datetime.today().year,
    #                       datetime.today().month,
    #                       datetime.today().day,
    #                       tzinfo=reference.LocalTimezone()) - timedelta(days=7)
    # end_date = datetime(datetime.today().year,
    #                     datetime.today().month,
    #                     datetime.today().day,
    #                     tzinfo=reference.LocalTimezone())
    # print start_date
    # print end_date
    # name_list = uncheck_clazz_users(clazz_list[8].id, start_date, end_date, 4)
    # print len(name_list)
    # content_list = []
    # for user in name_list:
    #     content_list.append(user.csv_format())
    # export_service.export2csv('Eng.csv', content_list)
