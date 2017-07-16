#!/usr/bin/python
# -*- coding: utf-8 -*-

from service import clazz_service


# 班级数
# 返回值：平台开设班级的数量
# 返回类型：int
def clazz_count():
    return (len(clazz_service.get_class_count()))


if __name__ == "__main__":
    print clazz_count()
