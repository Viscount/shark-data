#!/usr/bin/python
# -*- coding: utf-8 -*-

from metric import clazz_metric, user_metric, operation_metric


if __name__ == '__main__':
    # 班级数量
    # print clazz_metric.clazz_count_series()
    # 关注用户数量
    print user_metric.subscribe_user_count_series()
    # 付费用户数量
    # print user_metric.paid_user_count_series()
    # 客单数量
    # print operation_metric.purchase_count_series()
