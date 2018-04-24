#!/usr/bin/python
# -*- coding: utf-8 -*-


class Coupon(object):
    def __init__(self, query_result_item):
        self.id = query_result_item[0]
        self.money = query_result_item[1]
        self.expireDate = query_result_item[2]
        self.remark = query_result_item[3]
        self.status = query_result_item[4]
        self.objectId = query_result_item[5]
        self.userId = query_result_item[6]
