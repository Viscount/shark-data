#!/usr/bin/python
# -*- coding: utf-8 -*-


class Clazz(object):
    def __init__(self, query_result_item):
        self.id = query_result_item["_id"]
        self.status = query_result_item["status"]
        self.start_date = query_result_item["startDate"]
        self.clazz_type = query_result_item["clazzType"]
        self.end_date = query_result_item["endDate"]
        self.name = query_result_item["name"]
        self.author = query_result_item["author"]
        self.open_date = query_result_item["openDate"]
