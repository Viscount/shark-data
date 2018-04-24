#!/usr/bin/python
# -*- coding: utf-8 -*-


class UserPay(object):
    def __init__(self, query_result_item):
        self.id = query_result_item[0]
        self.out_biz_id = query_result_item[5]
        self.status = query_result_item[7]
        self.userId = query_result_item[10]

