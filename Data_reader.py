import zipfile
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
def read_data(js_files_path):
    # print(zipfile.is_zipfile(zipfilename))
    zfile = zipfile.ZipFile('Twitter data.zip', mode='r')  # 打开zip文件 并只读
    # print(zfile)
    with zipfile.ZipFile('Twitter data.zip', mode='r') as zfile:
        zfile.extractall()  # 在当前目录解压全部

        for name in zfile.namelist():  # allfile 是解压出所有zip后都json文件 name是在循环中遍历zfile的namelist
            allfile = zipfile.ZipFile(name, 'r')
            if '.zip' not in name:
                continue
            else:
                allfile.extractall()

    json_files_list = [js_files_path + '/' + i for i in os.listdir(js_files_path)]

    data = None

    for path in json_files_list:
        temp_df = pd.read_json(path, lines=True)
        if data is None:
            data = pd.DataFrame(columns=list(temp_df.columns))
        else:
            pass
            data = pd.concat([data, temp_df], axis=0)
    data.to_csv('/Users/jiayi/PycharmProjects/data/data.csv')
    return data