#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

def check_proxy(proxy,check_url = "http://www.qq.com/"):
    proxies_i = {
        "http":'http://'+proxy,
        "https":'https://'+proxy
    }
    headers_check = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
    }    
    try :
        requests.get(url = check_url,proxies = proxies_i,headers = headers_check,timeout=1)
    except :
        print(r"bad proxy : " + proxy)
        return False
    print(r"value proxy : " + proxy)
    return True