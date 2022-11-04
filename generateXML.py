"""
!/usr/bin/env python 3
-*- coding: utf-8 -*-
@File  : generateXML.py
@Author: GinaChou
@Date  : 2022/11/4
"""

from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree
from xml.etree import ElementTree  # 匯入ElementTree模組
from xml.dom import minidom

# generate root node
root = Element('root')

# generate first child-node head
head = SubElement(root, 'head')

# child-node of head node
title = SubElement(head, 'title')
title.text = "Well Dola!"

# generate second child-node body
body = SubElement(root, 'body')
body.text = "I Love Dola!"

tree = ElementTree(root)

# write out xml data
tree.write('result.xml', encoding = 'utf-8')

# elemnt為傳進來的Elment類，參數indent用於縮排，newline用於換行
def prettyXml(element, indent, newline, level=0):
    # 判斷element是否有子元素
    if element:
        # 如果element的text沒有內容
        if element.text == None or element.text.isspace():
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
            # 此處兩行如果把註釋去掉，Element的text也會另起一行
    # else:
    # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)  # 將elemnt轉成list
    for subelement in temp:
        # 如果不是list的最後一個元素，說明下一個行是同等級元素的起始，縮排應一致
        if temp.index(subelement) < (len(temp) - 1):
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最後一個元素， 說明下一行是母元素的結束，縮排應該少一個
            subelement.tail = newline + indent * level
            # 對子元素進行遞迴操作
        prettyXml(subelement, indent, newline, level=level + 1)


tree = ElementTree.parse('result.xml')  # 解析test.xml這個檔案，該檔案內容如上文
root = tree.getroot()  # 得到根元素，Element類
prettyXml(root, '\t', '\n')  # 執行美化方法

# ElementTree.dump(root)                 #顯示出美化後的XML內容

tree.write('result.xml', encoding='utf-8')


##https://zhuanlan.zhihu.com/p/54269963