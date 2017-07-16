#!/usr/bin/python
# -*- coding: utf-8 -*-

from service import purchase_service


# 付费用户数
# 返回值：平台中至少参与了一个班级的用户数量
# 返回类型：int
def paid_user_count():
    record_list = purchase_service.get_purchase_records()
    user_set = set()
    for record in record_list:
        user_set.add(record.userId)
    return len(user_set)


if __name__ == "__main__":
    print paid_user_count()
