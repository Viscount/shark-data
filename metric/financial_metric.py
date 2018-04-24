#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from service import user_service, purchase_service, coupon_service, pay_service
from util import export_service

TABLE_HEADER = ["昵称", "学号", "支付金额", "优币使用金额", "优惠券金额", "加入时间"]


def check_actual_pay(bill_info, outBizId):
    if bill_info["money"] == 0:
        return True
    actual_pay_info = pay_service.get_user_pay_records_by_outBizId(outBizId)
    for pay_record in actual_pay_info:
        if pay_record.status != "PAYING":
            return True
    return False


# 输出班级账单
# 参数：课程ID，保存路径
# 参数类型：string, string
# 返回值：无
def financial_detail(clazz_id, path):
    record_list = purchase_service.get_purchase_records_for_clazz(clazz_id)
    content_list = [TABLE_HEADER]
    for record in record_list:
        if record.bill is None:
            continue
        bill_info = json.loads(record.bill)
        if not check_actual_pay(bill_info, record.id):
            continue
        user = user_service.get_user_by_id(record.userId)
        content = user.csv_format()
        pay_info = [bill_info["money"]/100]
        if bill_info["coin"]["selected"]:
            pay_info.append(bill_info["coin"]["coin"])
        else:
            pay_info.append(0)
        if bill_info["coupon"]["selected"]:
            coupon = coupon_service.get_coupon_by_id(bill_info["coupon"]["id"])
            if coupon is None:
                pay_info.append("Unknown")
            else:
                pay_info.append(coupon.money)
        else:
            pay_info.append(0)
        content.extend(pay_info)
        content.append(record.joinDate)
        content_list.append(content)
    export_service.export2csv(path, content_list)
    return


if __name__ == "__main__":
    financial_detail("5a74243fb0ebed2f9fec62e4", "Trados.csv")
