#!/usr/bin/python
# -*- coding: utf-8 -*-


class User(object):
    def __init__(self, query_result_item):
        self.id = query_result_item[0]
        self.name = query_result_item[1]
        self.student_number = query_result_item[12]
        self.openId = query_result_item[16]
        self.unionId = query_result_item[17]
