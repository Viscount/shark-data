#!/usr/bin/python
# -*- coding: utf-8 -*-


class Checkin(object):
    def __init__(self, query_result_item):
        self.id = query_result_item["_id"]
        self.status = query_result_item["status"]
        self.userId = query_result_item["userId"]
        self.clazzId = query_result_item["clazz"]
        self.checkin_time = query_result_item["checkinTime"]

    def csv_format(self):
        content = [self.id, self.userId, self.status, self.checkin_time]
        return content
