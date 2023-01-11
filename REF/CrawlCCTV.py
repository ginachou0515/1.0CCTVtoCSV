"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@File  : CrawlCCTV.py
@Author: GinaChou
@Date  : 2022/10/21
"""
import requests
import xmltodict


def get_xmltodict(url):
    # 讀取線上XML資料，將XML轉換成Python的字典格式
    html = requests.get(url).text

    data = xmltodict.parse(html)
    stops = data["cctvinfo"]["cctv"]

    for stop in stops:
        videoUrl = stop["videoUrlHttps"]
        # print(f'種類={type(stop["@eqId"])}\n')
        print(
            f'eqId = {stop["@eqId"]} freewayId={stop["@freewayId"]} pmileage={stop["@pmileage"]} url={videoUrl["@url"]}')


def download_xml(url):
    response = requests.get(url)
    Result_Name = "1day_cctv_config_data.xml"
    with open(Result_Name, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':

    URL = "http://210.241.131.244/xml/1day_cctv_config_data_https.xml"

    # get_xmltodict(URL)
    download_xml(URL)
