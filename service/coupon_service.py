#!/usr/bin/python
# -*- coding: utf-8 -*-

from entity.coupon import Coupon
from connection.connector_singleton import *


def get_coupon_by_id(coupon_id):
    model = MysqlConnModel.get_instance()
    coupon = model.find("coupon", {"id": coupon_id}, multi=False)
    if len(coupon) < 1:
        return None
    else:
        return Coupon(coupon[0])
