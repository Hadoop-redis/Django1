#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: tianwen
@file: csv.py
@time: 2020/9/8 16:44
@desc: 将数据库的数据保存为csv文件
    https://blog.csdn.net/u014535666/article/details/105064898
"""

import pymysql
import csv


def from_mysql_get_all_info():
    conn = pymysql.connect(
        host='192.168.11.128',
        port=3306,
        user='root',
        db='linux',
        password='root',
        charset='utf8mb4',
    )
    cursor = conn.cursor()
    sql = "select * from linux;"
    cursor.execute(sql.encode('utf-8'))
    data = cursor.fetchone()
    conn.close()
    return data


def write_csv():
    data = from_mysql_get_all_info()
    filename = 'D:/file/linux.csv'
    with open(filename, mode='w', encoding='utf-8') as f:
        write = csv.writer(f, dialect='excel')
        for item in data:
            write.writerow(item)


if __name__ == '__main__':
    write_csv()
