#!/usr/bin/python
# -*- coding: utf-8 -*-


class User(object):
    def __init__(self, query_result_item):
        self.id = query_result_item[0]
        self.name = query_result_item[1]
        self.city = query_result_item[8]
        self.sex = query_result_item[10]
        self.student_number = query_result_item[12]
        self.openId = query_result_item[16]
        self.unionId = query_result_item[17]
        self.created_at = query_result_item[22]

    def csv_format(self, privacy=False):
        if privacy:
            content = [self.id, self.sex, self.city, self.student_number, self.created_at]
        else:
            content = [unicode(self.name), self.student_number, self.created_at]
        return content
