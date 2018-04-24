#!/usr/bin/python
# -*- coding: utf-8 -*-

from connection.connector_singleton import *
from entity.user_pay import UserPay


def get_user_pay_records_by_outBizId(outBizId):
    model = MysqlConnModel.get_instance()
    records = model.find("user_pay", {"outBizId": outBizId}, multi=True)
    user_pay_records = [UserPay(record) for record in records]
    return user_pay_records


if __name__ == "__main__":
    print get_user_pay_records_by_outBizId(15850)
