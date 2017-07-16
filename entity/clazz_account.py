#!/usr/bin/python
# -*- coding: utf-8 -*-


class ClazzAccount(object):
    def __init__(self, query_result_item):
        self.id = query_result_item[0]
        self.bill = query_result_item[2]
        self.status = query_result_item[3]
        self.joinDate = query_result_item[4]
        self.userId = query_result_item[7]
        self.clazzId = query_result_item[9]
        self.createdAt = query_result_item[16]


