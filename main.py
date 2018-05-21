#!/usr/bin/python3
# -*- coding: utf-8 -*-


import threading

from insert_value_proxy import *
from web_port import *

a = threading.Thread(target=star_flask)
b = threading.Thread(target=insert_value_proxy)
b.start()
star_flask()



#增加代理获取网页
#增加定期检查筛选后的代理

