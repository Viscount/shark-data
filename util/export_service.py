#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import csv


def export2csv(file_name, content_list):
    with codecs.open(file_name, "wb", encoding="utf-8") as f:
        csv_writer = csv.writer(f, dialect='excel')
        for content in content_list:
            csv_writer.writerow(content)
    return
