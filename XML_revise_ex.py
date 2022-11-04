"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@File  : XML_revise_ex.py
@Author: GinaChou
@Date  : 2022/11/4
"""

"""
ElementTree模塊提供多種修改xml的方法
1、ElementTree.write("xmlfile") #更新xml檔案
2、Element.append():為當前的element新增子元素
3、Element.set(key,value):為當前的element的key屬性設置value值
4、Element.remove(element):刪除為element的節點
https://cloud.tencent.com/developer/article/1975193
"""

# 匯入模組
import os
import xml.etree.ElementTree as ET
# 讀取將被修改的檔案並獲取根節點
tree =ET.parse("new.xml")
root=tree.getroot()

#建立新節點sub_new,新增屬性和資料，並將其設定為root的子節點
sub_new=ET.Element("sub_new")
sub_new.attrib={"name":"000000000004"}
sub_new.text="new element"
root.append(sub_new)

#修改sub1的attribute屬性,比如name更新為新的編號
sub1=root.find("sub1")
sub1.set("attribute","new attribute")

#修改sub2的資料
sub2=root.find("sub2")
sub2.text="new value"

#刪除子節點sub3
sub3=root.find("sub3")
root.remove(sub3)

tree.write("new.xml")

# 應用一：xml節點插入、修改、刪除操作
# 場景一：指定位置插入、修改、刪除節點
#指定位置插入節點
tree =ET.parse("new_test.xml")
root=tree.getroot()

#獲取data下所有的節點
lst=root.findall("data")
lst1=lst[0].findall("meter")

# 建立一個新節點meter_new
sub_new=ET.Element("meter_new")
sub_new.attrib={"name":"000000000004"}
#將function_new設定為meter_new的子節點，新增屬性和資料
sub_new1=ET.SubElement(sub_new,"function_new")
sub_new1.attrib={"name":"000000000004-1090"}
sub_new1.text="90"

#指定位置插入
lst1.insert(0,sub_new)
print(lst1)

#刪除data節點歷史資料
sub=root.find("data")
root.remove(sub)

#建立新節點data
data=ET.SubElement(root,"data")
#新增節點
[data.append(i) for i in lst1]
#寫入更新xml
tree.write("new_test1.xml")

# 應用二：多個xml數據包合併操作
# 場景二：同一時刻多個數據xml合併
## 合併xml結構如下
def xml_combine(xml_dir):
    # 建立根節點,根據xml結構樣式設定即可
    root=ET.Element("root")
    tree = ET.ElementTree(root)
    #建立子節點data
    data = ET.SubElement(root, "data")
    xml_data = [i for i in os.listdir(xml_dir)]
    xml_list=[]
    for i in range(len(xml_data)):
        # 讀取將被修改的檔案並獲取根節點
        tree_ = ET.parse(xml_dir+"\{0}".format(xml_data[i]))
        root_ = tree_.getroot()
        # 獲取data下所有的節點
        lst = root_.findall("data")
        lst1 = lst[0].findall("meter")
        #meter節點合併成一個列表
        xml_list.extend(lst1)
    #新增節點
    [data.append(i) for i in xml_list]
    # 寫入更新xml
    tree.write("xml_combine.xml")

if __name__ == '__main__':
    xml_dir = r"D:\myProjectfile\xml_parse\xml"
    xml_combine(xml_dir)