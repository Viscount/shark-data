#!/usr/bin/python
# -*- coding: utf-8 -*-

from service import purchase_service


def paid_user_list():
    record_list = purchase_service.get_purchase_records()
    user_set = set()
    for record in record_list:
        user_set.add(record.userId)
    return user_set


if __name__ == "__main__":
    print len(paid_user_list())
