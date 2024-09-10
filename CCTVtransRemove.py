"""
!/usr/bin/env python 3.9
-*- coding: utf-8 -*-
@File  : CCTVtrans.py
@Author: GinaChou
@Date  : 2022/12/06
"""

import requests
import xmltodict
import os
import xml.etree.ElementTree as ET

def download_xml(url):
    response = requests.get(url)
    Result_Name = "1day_cctv_config_data_https.xml"
    with open(Result_Name, 'wb') as file:
        file.write(response.content)
    print(f'下載1天全部設備：1day_cctv_config_data_https.xml')

def url_xml_dict(url):
    '''讀取並解析線上xml
       url: xml網址
       return: XML轉換成Python的字典格式'''
    html = requests.get(url)
    html.encoding = html.apparent_encoding ##內容解碼跟編碼不一致 1130607
    data = xmltodict.parse(html.text)
    return data

if __name__ == '__main__':
    # URL = "http://210.241.131.244/xml/1day_cctv_config_data_https.xml"
    URL = "https://tisv.tcloud.freeway.gov.tw/xml/cloud_00/1day_cctv_config_data_https.xml"
    download_xml(URL)

    data = url_xml_dict(URL)
    info = data["cctvinfo"]
    stops = data["cctvinfo"]["cctv"]

    root = ET.Element(
        'XML_Head',
        attrib={
            "version": "1.1",
            "listname": "CCTV靜態資訊",
            "updatetime": info["@time"],
            "interval": "86400"})

    Infos = ET.SubElement(root, 'Infos')

    for stop in stops:##0526修改為以包含標頭設備判斷
        if "0" in stop["@enabled"]: #移除不發表於1968的設備
            print(f'不發表於1968：{stop["@eqId"]}')
            continue
        if "CCTV-T62" in stop["@eqId"]:#移除公總管理的設備
            print(f'不含台62：{stop["@eqId"]}')
            continue
        if "CCTV-T64" in stop["@eqId"]:#移除公總管理的設備
            print(f'不含台64：{stop["@eqId"]}')
            continue
        if "CCTV-T66" in stop["@eqId"]:#移除公總管理的設備
            print(f'不含台66：{stop["@eqId"]}')
            continue
        if "CCTV-T68" in stop["@eqId"]:#移除公總管理的設備
            print(f'不含台68：{stop["@eqId"]}')
            continue
        Info = ET.Element(
            'Info', {
                "cctvid":"nfb"+str(stop["@eqId"]),
                "roadsection":"0",
                "locationpath":"0",  ##給""會出現locationpath錯誤，推測是因為屬性
                "startlocationpoint":"0",
                "endlocationpoint":"0",
                "px":str(stop["@longitude"]),
                "py":str(stop["@latitude"])})

        Infos.append(Info)

    tree = ET.ElementTree(root)

    tree.write(os.path.join(os.path.dirname(__file__), "cctv_info_0000.xml"))
    print(f'{info["@time"]}\n輸出更新CCTV檔：cctv_info_0000.xml')


"""JAVA設定的屬性如下：
        # String cctvid;
		# String roadsection;
		# int locationpath;
		# int startlocationpoint;
		# int endlocationpoint;
		# float px;
		# float py;
"""