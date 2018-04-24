#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import *
from service import purchase_service
from util import date_service


# 购买次数
def purchase_count(start_date="2016-01-01", end_date=datetime.now().strftime("%Y-%m-%d")):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    purchase_list = purchase_service.get_purchase_records(start_date, end_date)
    return len(purchase_list)


# 购买次数，按月统计
def purchase_count_series(start_date="2016-07-01"):
    timeline = date_service.get_between_month(start_date)
    purchase_count_dict = dict()
    for month in timeline:
        purchase_count_dict[month.name] = len(purchase_service.get_purchase_records(end_date=month.start_date))
    return purchase_count_dict


# 总体复购率
# 返回值：（一次购买率，二次购买率，多次购买率）
# 返回类型：tuple
def overall_re_purchasing_rate():
    purchase_record_list = purchase_service.get_purchase_records()
    user_paid_count = dict()
    for record in purchase_record_list:
        if str(record.userId) in user_paid_count:
            user_paid_count[str(record.userId)] += 1
        else:
            user_paid_count[str(record.userId)] = 1

    # 将用户-购买次数统计归类到三项指标计数

    one_time_count = 0
    two_times_count = 0
    multi_times_count = 0
    for userId in user_paid_count:
        paid_count = user_paid_count[userId]
        if paid_count == 1:
            one_time_count += 1
        elif paid_count == 2:
            two_times_count += 1
        elif paid_count > 2:
            multi_times_count += 1
    total_user_count = len(user_paid_count)
    one_time_ptg = one_time_count * 1.0 / total_user_count
    two_times_ptg = two_times_count * 1.0 / total_user_count
    multi_times_ptg = multi_times_count * 1.0 / total_user_count
    return one_time_ptg, two_times_ptg, multi_times_ptg


# 新老学员比例
# 参数：统计区间天数，如30就是一月内
# 参数类型：int
# 返回值：（新学员比例，老学员比例）
# 返回类型：tuple
def student_type_ratio(time_backward_days=30):
    time_constraint = datetime.today()-timedelta(days=time_backward_days)
    purchase_record_list = purchase_service.get_purchase_records()
    # 从购买列表中按时间分离出统计范围内和统计范围外的用户并计数
    in_bound_user_count = set()
    out_bound_user_count = set()
    for record in purchase_record_list:
        if record.joinDate > time_constraint:
            in_bound_user_count.add(record.userId)
        else:
            out_bound_user_count.add(record.userId)
    re_purchase_user_count = 0
    for userId in in_bound_user_count:
        if userId in out_bound_user_count:
            re_purchase_user_count += 1
    frequent_student_ratio = re_purchase_user_count * 1.0 / len(in_bound_user_count)
    new_student_ratio = 1 - frequent_student_ratio
    return new_student_ratio, frequent_student_ratio


# 复购人次
# 参数：统计区间天数，如30就是一月内
# 参数类型：int
# 返回值：（新学员比例，老学员比例）
# 返回类型：tuple
def re_purchase_count(time_backward_days=30):
    time_constraint = datetime.today()-timedelta(days=time_backward_days)
    purchase_record_list = purchase_service.get_purchase_records()
    # 从购买列表中按时间分离出统计范围内和统计范围外的用户并计数
    in_bound_user_pay_count = dict()
    out_bound_user_pay_count = dict()
    for record in purchase_record_list:
        if record.joinDate > time_constraint:
            if str(record.userId) in in_bound_user_pay_count:
                in_bound_user_pay_count[str(record.userId)] += 1
            else:
                in_bound_user_pay_count[str(record.userId)] = 1
        else:
            if str(record.userId) in out_bound_user_pay_count:
                out_bound_user_pay_count[str(record.userId)] += 1
            else:
                out_bound_user_pay_count[str(record.userId)] = 1
    re_purchase_times_count = 0
    for userId in in_bound_user_pay_count:
        pay_count = in_bound_user_pay_count[userId]
        if userId in out_bound_user_pay_count:
            re_purchase_times_count += pay_count
    return re_purchase_times_count


if __name__ == "__main__":
    # 购买次数
    # print purchase_count(start_date="2017-08-23")
    # 总体复购率
    # print overall_re_purchasing_rate()
    # 新老学员比例
    # print student_type_ratio(180)
    # 复购次数5
    print re_purchase_count(180)
