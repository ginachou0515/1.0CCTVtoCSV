"""
!/usr/bin/env python 3.9
-*- coding: utf-8 -*-
@File  : CCTVtrans.py
@Author: GinaChou
@Date  : 2022/10/21
"""

import requests
import xmltodict
import os
import xml.etree.ElementTree as ET

def download_xml(url):
    response = requests.get(url)
    Result_Name = "1day_cctv_config_data.xml"
    with open(Result_Name, 'wb') as file:
        file.write(response.content)

def url_xml_dict(url):
    '''讀取並解析線上xml
       url: xml網址
       return: XML轉換成Python的字典格式'''
    html = requests.get(url)
    data = xmltodict.parse(html.text)
    return data

if __name__ == '__main__':

    URL = "http://210.241.131.244/xml/1day_cctv_config_data_https.xml"
    # download_xml(URL)

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
    ##
    for stop in stops:
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

    tree.write(os.path.join(os.path.dirname(__file__), "newCCTVto1.1.xml"))


"""JAVA設定的屬性如下：
        # String cctvid;
		# String roadsection;
		# int locationpath;
		# int startlocationpoint;
		# int endlocationpoint;
		# float px;
		# float py;
"""