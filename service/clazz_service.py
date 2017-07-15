#!/usr/bin/python
# -*- coding: utf-8 -*-

import connection.mongo
from connection.model import MongoModel


def get_class_count():
    mongo_mc = connection.mongo.MongoConnector()
    mongo_mm = MongoModel(mongo_mc)
    clazz_list = mongo_mm.find('Clazz', {}, multi=True)
    return clazz_list
