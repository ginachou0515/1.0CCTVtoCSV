
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import requests
import xmltodict as xdict
import json
import csv
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET


def get_xml():
    # 讀取線上XML資料，將XML轉換成Python的字典格式
    url = "http://210.241.131.244/xml/1day_cctv_config_data_https.xml"
    html = requests.get(url).text
    data = xdict.parse(html)
    stops = data["cctvinfo"]["cctv"]
    for stop in stops:
        print(f'{stop["@eqId"]} mile={stop["@pmileage"]}')
        gifUrl = stop["gifUrl"]
        print(f'url={gifUrl["@url"]}')


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    #    get_xml()
    url = "http://210.241.131.244/xml/1day_cctv_config_data_https.xml"
    data = requests.get(url)
    xpars = xdict.parse(data.text)
    # print(type(xpars)) #中文
    # print(xpars)  # 中文
    # json庫dumps()是將dict轉化成json格式，loads()是將json轉化成dict格式。
    # dumps()方法的ident=1，格式化json
    jsonstr = json.dumps(
        xpars,
        indent=1,
        ensure_ascii=False)  # indent參數決定添加幾個空格
    # Python 3中的json在做dumps操作時，會將中文轉換成unicode編碼，並以16進制方式儲存，再做逆向操作時，會將unicode編碼轉換回中文
    # 輸出JSON
    with open("text.json", "w", encoding="utf-8") as f:
        f.write(jsonstr)
    f.close()

    stops = xpars["cctvinfo"]["cctv"]
    # print(f'{stops}')
    xml_list = []
    column_name = [
        'dbId',
        'domainId',
        'eqId',
        'freewayId',
        'latitude',
        'locationId',
        'longitude',
        'mainDirection',
        'url']
    # list_is_none = lambda x: x[0] if x else ""
    for stop in stops:
        videoUrl = stop["videoUrlHttps"]
        # print(f'種類={type(stop["@eqId"])}\n')
        print(
            f'eqId = {stop["@eqId"]} freewayId={stop["@freewayId"]} pmileage={stop["@pmileage"]} url={videoUrl["@url"]}')
        value = (
            stop["@dbId"],
            stop["@domainId"],
            stop["@eqId"],
            stop["@freewayId"],
            stop["@latitude"],
            stop["@locationId"],
            stop["@longitude"],
            stop["@mainDirection"],
            videoUrl["@url"]
        )
        xml_list.append(value)

    xml_df = pd.DataFrame(xml_list, columns=column_name)
    xml_df.to_csv('newCCTV.csv', encoding="utf-8", index=None)
    # EXCL要另存為ANSI


# encode('utf-8').decode('utf-8')
# encode('utf-8').decode('unicode_escape')
