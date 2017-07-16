#!/usr/bin/python
# -*- coding: utf-8 -*-

import connection.mysql
from connection.model import MySQLModel


def get_users():
    mysql_mc = connection.mysql.MySQLConnector()
    mysql_mm = MySQLModel(mysql_mc)
    user_list = mysql_mm.find("user", {}, multi=True)
    return user_list


if __name__ == "__main__":
    print len(get_users())
