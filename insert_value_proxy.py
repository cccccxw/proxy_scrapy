#!/usr/bin/python3
# -*- coding: utf-8 -*-

from db.check_proxy import check_proxy
from db.get_one_proxy import get_one_proxy
from db.value_proxy import value_proxy
import time

def insert_value_proxy():
    while 1:
        if value_proxy('')<20:
            proxy = get_one_proxy()
            if check_proxy(proxy):
                value_proxy(proxy)
            else:
                insert_value_proxy()
        time.sleep(1)

if __name__ == '__main__':
    insert_value_proxy()
