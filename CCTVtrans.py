"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@File  : CCTVtrans.py
@Author: GinaChou
@Date  : 2022/11/4
"""

import requests
import xmltodict
import json
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


def download_xml(url):
    response = requests.get(url)
    Result_Name = "1day_cctv_config_data.xml"
    with open(Result_Name, 'wb') as file:
        file.write(response.content)


def xmltojson(xml, output):
    path = os.getcwd()
    xml_str = os.path.join(path, xml)
    with open(xml_str, 'rb') as data:
        xml_parse_dict = xmltodict.parse(data)
        print(xml_parse_dict)

    jsonstr = json.dumps(
        xml_parse_dict,
        indent=1,
        ensure_ascii=False)  # indent參數決定添加幾個空格
    # Python 3中的json在做dumps操作時，會將中文轉換成unicode編碼，並以16進制方式儲存，再做逆向操作時，會將unicode編碼轉換回中文
    # 輸出JSON
    json_name = os.path.join(path, f"{output}.json")
    with open(json_name, "w", encoding="utf-8") as f:
        f.write(jsonstr)
    f.close()


if __name__ == '__main__':

    URL = "http://210.241.131.244/xml/1day_cctv_config_data_https.xml"
    # download_xml(URL)

    xml1 = "cctv_info_0000.xml"
    output1 = "CCTV1.1"
    xml2 = "1day_cctv_config_data.xml"
    output2 = "CCTV2.0"
    # xmltojson(xml1, output1)
    # xmltojson(xml2, output2)

    # 建立根節點 與屬性
    root = ET.Element(
        'XML_Head',
        attrib={
            "version": "1.1",
            "listname": "CCTV靜態資訊",
            "updatetime": "2022/11/04 12:00:00",
            "interval": "86400"})

    Infos = ET.SubElement(root, 'Infos')
    a = "CCTV-test"
    longitude = "121"
    latitude = "22"
    Infos = ET.SubElement(
        Infos, "Info", {
            "cctvid": a,
            "roadsection": "",
            "locationpath": "",
            "startlocationpoint": "",
            "endlocationpoint": "",
            "px": longitude,
            "py": latitude})

    tree = ET.ElementTree(root)
    print(f"tree{tree}")
    tree.write(os.path.join(os.path.dirname(__file__), "test1.1.xml"))

    # # 將根目錄轉化為樹行結構
    # tree = ET.ElementTree(root)
    # rough_str = ET.tostring(root, 'utf-8')
    # # 格式化
    # reparsed = minidom.parseString(rough_str)
    # new_str = reparsed.toprettyxml(indent='\t')
    # f = open('test.xml', 'w', encoding='utf-8')
    # # 保存
    # f.write(new_str)
    # f.close()


# 讀取CCTV 標籤
    # tree = ET.ElementTree(file=xml1)
    # tree.getroot()
    # root = tree.getroot()
    # print(f"root.tag{root.tag}\nroot.attrib:{root.attrib}")
    #
    # # for child_of_root in root:
    # #     print(
    # #         f"child_of_root.tag{child_of_root.tag}\tchild_of_root.attrib:{child_of_root.attrib}")
    # for elem in tree.iterfind('Infos/Info'):
    #     print(
    #         f"elem.tag:{elem.tag}\telem.attrib:{elem.attrib}")
