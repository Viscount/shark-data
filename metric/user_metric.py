#!/usr/bin/python
# -*- coding: utf-8 -*-

from service import user_service


def paid_user_count():
    record_list = user_service.get_paid_users()
    user_set = set()
    for record in record_list:
        user_set.add(record[7])
    return len(user_set)


if __name__ == "__main__":
    print paid_user_count()
