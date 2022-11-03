
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import requests
import xmltodict as xdict
import json
import csv
import pandas as pd
import numpy as np



def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

def get_xml():
    #讀取線上XML資料，將XML轉換成Python的字典格式
    url = "http://210.241.131.244/xml/1day_cctv_config_data_https.xml"
    html = requests.get(url).text
    data = xdict.parse(html)
    stops = data["cctvinfo"]["cctv"]
    for stop in stops:
        print(f'{stop["@eqId"]} mile={stop["@pmileage"]}')
        gifUrl = stop["gifUrl"]
        print(f'url={gifUrl["@url"]}')
    # stops = data["cctvinfo"]["cctv"]
    # for stop in stops:
    #     print(f'Hi,{stop["@eqId"]}, {stop["@pmileage"]}')

def xmltocsv(jsonfile):##格式有問題
    #讀取線上XML資料，將XML轉換成csv
    url = "http://210.241.131.244/xml/1day_cctv_config_data_https.xml"
    html = requests.get(url)
    xmlparse = xdict.parse(html).txt
    # json庫dumps()是將dict轉化成json格式，loads()是將json轉化成dict格式。
    # dumps()方法的ident=1，格式化json
    jsonstr = json.dumps(xmlparse, indent=1)

    # with open(jsonfile, "w", encoding="utf-8") as f:
    #   f.write(jsonstr)
    pdObj = pd.read_json(jsonstr, orient='index')
    print(pdObj)



        
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
#    get_xml()
#    xmltocsv("samplecsv.csv")

    url = "http://210.241.131.244/xml/1day_cctv_config_data_https.xml"
    data = requests.get(url)
    xpars = xdict.parse(data.text)
    # json庫dumps()是將dict轉化成json格式，loads()是將json轉化成dict格式。
    # dumps()方法的ident=1，格式化json
    jsonstr = json.dumps(xpars, indent=1)  ##indent參數決定添加幾個空格

    # ##輸出JSON
    # with open("text.json", "w", encoding="utf-8") as f:
    #   f.write(jsonstr)
    # f.close()

    fieldnames = ['dbId', 'domainId', 'eqId', 'freewayId', 'latitude', 'locationId', 'longitude', 'mainDirection',
                   'url']  # 定義要寫入資料的鍵

    # data1 = np.arange(10)
    # data2 = np.arange(10) * 2
    # data3 = np.arange(10) * 3
    # writefile = '../test.csv'
    # with open(writefile, 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(fieldnames)
    #     writer.writerows(zip(data1, data2, data3))
    # stops = xpars["cctvinfo"]["cctv"]
    # for stop in stops:
    #     gifUrl = stop["gifUrl"]
    #     # print(f'{stop["@eqId"]} mile={stop["@pmileage"]}')
    #     # print(f'url={gifUrl["@url"]}')
    #
    #     value = (stop["@dbId"],
    #              stop["@domainId"],
    #              stop["@eqId"],
    #              stop["@freewayId"],
    #              stop["@latitude"],
    #              stop["@locationId"],
    #              stop["@longitude"],
    #              stop["@mainDirection"],
    #              gifUrl["@url"]
    #              )
    #     xml_list.append(value)
    # # column_name = ['dbId', 'domainId', 'eqId', 'freewayId', 'latitude', 'locationId', 'longitude', 'mainDirection', 'url']
    # xml_df = pd.DataFrame(xml_list, columns=column_name)
    # xml_df.to_csv('newCCTV.csv', encoding="utf-8", index=None)


    stops = xpars["cctvinfo"]["cctv"]
    # print(f'{stops}')
    xml_list = []
    column_name = ['dbId', 'domainId', 'eqId', 'freewayId', 'latitude', 'locationId', 'longitude', 'mainDirection',
                   'url']
    for stop in stops:
        gifUrlHttps = stop["gifUrlHttps"]
        # print(f'{stop["@eqId"]} mile={stop["@pmileage"] url={gifUrl["@url"]}')
        value = (stop["@dbId"],
                 stop["@domainId"],
                 stop["@eqId"],
                 stop["@freewayId"],
                 stop["@latitude"],
                 stop["@locationId"],
                 stop["@longitude"],
                 stop["@mainDirection"],
                 gifUrlHttps["@url"]
                 )
        xml_list.append(value)
    # column_name = ['dbId', 'domainId', 'eqId', 'freewayId', 'latitude', 'locationId', 'longitude', 'mainDirection', 'url']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    xml_df.to_csv('newCCTV.csv', encoding="utf-8", index=None)


    # list_is_none = lambda x: x[0] if x else ""

####(2)存為json檔案
    # url = "http://210.241.131.244/xml/1day_cctv_config_data_https.xml"
    # data = requests.get(url)
    # xpars = xdict.parse(data.text)
    # ##在此轉為json##
    # with open('new_data.json', 'w+') as json_file:
    #     json.dump(xpars, json_file, indent=4, sort_keys=True)





# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
