#!/usr/bin/python
# -*- coding: utf-8 -*-

from service import purchase_service


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


if __name__ == "__main__":
    print overall_re_purchasing_rate()
