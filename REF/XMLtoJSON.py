"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@File  : XMLtoJSON.py
@Author: GinaChou
@Date  : 2022/10/21
"""

## 1、使用xmltodict和json實現
import requests
import xmltodict, json
o = xmltodict.parse("""
<catalog>
    <maxid>4</maxid>
    <login username="pytest" passwd='123456'>
        <caption>Python</caption>
        <item id="4">
            <caption>測試</caption>
        </item>
    </login>
    <item id="2">
        <caption>Zope</caption>
    </item>
</catalog>
 """)
json.dumps(o) # '{"catalog": {"maxid": "4", "login": {"@username": "pytest", "@passwd": "123456", "caption": "Python", "item": {"@id": "4", "caption": "\\u6d4b\\u8bd5"}}, "item": {"@id": "2", "caption": "Zope"}}}'

# import xmltodict
# data = requests.get(url)
# xpars = xmltodict.parse(data.text)
# json = json.dumps(xpars)
# print json

# ## 2、使用xml.etree實現
# from xml.etree import ElementTree as ET
# xml = ET.parse('FILE_NAME.xml')
# def parseXmlToJson(xml):
#   response = {}
#   for child in list(xml):
#     if len(list(child)) > 0:
#       response[child.tag] = parseXmlToJson(child)
#     else:
#       response[child.tag] = child.text or ''
#   return response
#
# parsed = parseXmlToJson(xml)

# import xml.etree.ElementTree as ET
# import xmltodict
# import json
#
# tree = ET.parse('output.xml')
# xml_data = tree.getroot()
#
# xmlstr = ET.tostring(xml_data, encoding='utf8', method='xml')
#
#
# data_dict = dict(xmltodict.parse(xmlstr))
#
# print(data_dict)
#
# with open('new_data_2.json', 'w+') as json_file:
#     json.dump(data_dict, json_file, indent=4, sort_keys=True)
#
### 链接：https://juejin.cn/post/7044718932808171533

def xmltojson():
  import xml.etree.ElementTree as ET
  import xmltodict
  import json

  tree = ET.parse('output.xml')
  xml_data = tree.getroot()

  xmlstr = ET.tostring(xml_data, encoding='utf8', method='xml')

  data_dict = dict(xmltodict.parse(xmlstr))

  print(data_dict)

  with open('new_data_2.json', 'w+') as json_file:
    json.dump(data_dict, json_file, indent=4, sort_keys=True)

  ##  https: // juejin.cn / post / 7044718932808171533


import json
import xmltodict
import pandas as pd
# 定義xml轉json的函數

class Json_xml():
  def __init__(self):
    pass

  # xml轉json
  def xmltojson(self, xmlfile, jsonfile):
    xmlstr = ''
    with open(xmlfile, 'r', encoding='utf-8') as f:
      xmlstr = f.read()
    # parse是的xml解析器
    xmlparse = xmltodict.parse(xmlstr)
    # json庫dumps()是將dict轉化成json格式，loads()是將json轉化成dict格式。
    # dumps()方法的ident=1，格式化json
    jsonstr = json.dumps(xmlparse, indent=1)
    with open(jsonfile, "w", encoding="utf-8") as f:
      f.write(jsonstr)

  # json轉xml函數
  def jsontoxml(self, jsonfile, xmlfile):
    data = ''
    with open(jsonfile, 'r', encoding="utf-8") as f:
      data = json.load(f)
    xmlstr = xmltodict.unparse(data)
    with open(xmlfile, "w", encoding="utf-8") as f:
      f.write(xmlstr)

  # josn轉excel

  # json 轉excel
  def json_to_excel(self, jsonfile, excelfile):
    data = pd.read_json(jsonfile)
    data.to_excel(excelfile)

  # excel轉json
  def excel_to_json(self, excelfile, jsonfile):
    data = pd.read_excel(excelfile)
    data.to_json(jsonfile)

  # excel轉xml
  def excel_to_xml(self, excelfile, xmlfile):
    self.excel_to_json(excelfile, "text.json")
    self.jsontoxml("text.json", xmlfile)

  # xml轉excel
  def xml_to_excel(self, xmlfile, excelfile):
    self.xmltojson(xmlfile, "text.json")
    self.json_to_excel("text.json", excelfile)


if __name__ == "__main__":
  pass

##©著作权归作者所有：来自51CTO博客作者东方佑的原创作品，请联系作者获取轉载授权，否则將追究法律责任
