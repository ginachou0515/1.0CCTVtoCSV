"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@File  : CrawlCCTV.py
@Author: GinaChou
@Date  : 2022/10/21
"""
import requests
import xmltodict


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

def get_xml():
    #讀取線上XML資料，將XML轉換成Python的字典格式
    url = "http://210.241.131.244/xml/1day_cctv_config_data_https.xml"
    html = requests.get(url).text
    data = xmltodict.parse(html)
    stops = data["cctvinfo"]["cctv"]
    print(f'{stops}')
    # for stop in stops:
    #     print(f'{stop["@eqId"]} mile={stop["@pmileage"]}')
    #     gifUrl = stop["gifUrl"]
    #     print(f'url={gifUrl["@url"]}')
    # stops = data["cctvinfo"]["cctv"]
    # for stop in stops:
    #     print(f'Hi,{stop["@eqId"]}, {stop["@pmileage"]}')

if __name__ == '__main__':
    print_hi('PyCharm')
    get_xml()


