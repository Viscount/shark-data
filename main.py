#!/usr/bin/python
# -*- coding: utf-8 -*-

from metric import financial_metric


if __name__ == '__main__':
    # 班级账单
    financial_metric.financial_detail("5a74243fb0ebed2f9fec62e4", "./Trados.csv")
