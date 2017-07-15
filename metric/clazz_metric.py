#!/usr/bin/python
# -*- coding: utf-8 -*-

from service import clazz_service


def clazz_count():
    return (len(clazz_service.get_class_count()))


if __name__ == "__main__":
    print clazz_count()
