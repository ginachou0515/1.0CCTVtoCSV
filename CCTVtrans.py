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

def xmltojson(xml,output):
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
    json_name = os.path.join(path,f"{output}.json")
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
    xmltojson(xml1, output1)
    xmltojson(xml2, output2)


    # 建立根節點
    root = ET.Element('school')
    names = ['張三', '李四']
    genders = ['男', '女']
    ages = ['20', '18']
    # 新增子節點
    student1 = ET.SubElement(root, 'student')
    student2 = ET.SubElement(root, 'student')
    ET.SubElement(student1, 'name').text = names[0]
    ET.SubElement(student1, 'gender').text = genders[0]
    ET.SubElement(student1, 'age').text = ages[0]
    ET.SubElement(student2, 'name').text = names[1]
    ET.SubElement(student2, 'gender').text = genders[1]
    ET.SubElement(student2, 'age').text = ages[1]
    # 將根目錄轉化為樹行結構
    tree = ET.ElementTree(root)
    rough_str = ET.tostring(root, 'utf-8')
    # 格式化
    reparsed = minidom.parseString(rough_str)
    new_str = reparsed.toprettyxml(indent='\t')
    f = open('test.xml', 'w', encoding='utf-8')
    # 保存
    f.write(new_str)
    f.close()
