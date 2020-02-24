#回归数据预处理
import numpy as np
import pandas as pd
import json
#生成字典及编码
def gen_dict(data, filename):
    sets = list(set(data))
    dict_sets = {value: key for key, value in enumerate(sets)}
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(dict_sets, f)
def encode_data(data, dict_sets):
    new_data = [dict_sets[data[i]] for i in data.index]
    return new_data
if __name__ == '__main__':
    df = pd.read_csv('data/cls_data.csv', index_col=0)
    # #字典生成,随机生成的
    # gen_dict(df['area'], 'dict/area_dict.json')
    # gen_dict(df['house_type'], 'dict/house_type_dict.json')
    # gen_dict(df['floor'], 'dict/floor_dict.json')
    # 字典加载
    with open('dict/house_type_dict.json', 'r', encoding='utf-8') as f:
        house_type_dict = json.load(f)
    with open('dict/area_dict.json', 'r', encoding='utf-8') as f:
        area_dict = json.load(f)
    with open('dict/floor_dict.json', 'r', encoding='utf-8') as f:
        floor_dict = json.load(f)
    # print(area_dict)
    # print(floor_dict)
    # print(house_type_dict)
    # {'静安': 0, '黄浦': 1, '闸北': 2, '嘉定': 3, '宝山': 4, '上海周边': 5, '普陀': 6, '徐汇': 7, '长宁': 8, '松江': 9, '崇明': 10, '奉贤': 11, '杨浦': 12, '浦东': 13, '闵行': 14, '青浦': 15, '金山': 16, '虹口': 17}
    # {'中楼层': 0, '未知': 1, '高楼层': 2, '低楼层': 3}
    # {'3室2厅1卫': 0, '3室1厅1卫': 1, '2室2厅1卫': 2, '3室1厅2卫': 3, '2室1厅2卫': 4, '其他户型': 5, '4室2厅3卫': 6, '2室2厅2卫': 7, '3室2厅3卫': 8, '1室1厅1卫': 9, '4室2厅4卫': 10, '3室2厅2卫': 11, '1室0厅1卫': 12, '2室0厅1卫': 13, '1室2厅1卫': 14, '4室2厅2卫': 15, '2室1厅1卫': 16}
    df['area'] = encode_data(df['area'], area_dict)
    df['house_type'] = encode_data(df['house_type'], house_type_dict)
    df['floor'] = encode_data(df['floor'], floor_dict)
    # print(df)
    #one-hot化
    for i in ['area','house_type','floor','cls_result']:
        variable = pd.get_dummies(df[i], prefix=i)
        df = pd.concat([df, variable], axis=1)
        del df[i]
    print(df)
    #df.to_csv('data/reg_data.csv')
