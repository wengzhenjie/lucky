#数据预处理
import numpy as np
import pandas as pd
import re
if __name__ == '__main__':
    df = pd.read_csv('data/info.csv')
    data = pd.DataFrame()
    data['area'] = df['area']
    data['rent'] = df['rent']
    # 面积处理
    square = df['square']
    square = [int(i[:-1]) for i in square.values]
    square = pd.Series(square, index=df.index)
    data['square'] = square
    # 户型处理结合探索情况
    house_type = df['house_type']
    house_type_dt = house_type.value_counts()
    other_type = set(house_type_dt[16:].index)
    types = house_type.values
    for i, v in enumerate(types):
        if v in other_type:
            types[i] = '其他户型'
    house_type = pd.Series(types, index=df.index)
    data['house_type'] = house_type
    # 楼层处理结合探索情况
    floor = df['floor'].values
    # floor = pd.Series([i.split('/')[0] for i in floor])  # 预处理
    l = {'低楼层', '中楼层', '高楼层'}
    for i, v in enumerate(floor):
        fi = v.split('/')[0]
        if fi not in l:
            floor[i] = '未知'
        else:
            floor[i] = fi
    floor = pd.Series(floor, index=df.index)
    data['floor'] = floor
    # 地铁信息存在大量空数据，结合探索情况，将该列数据处理为二分类变量，即有无地铁
    subway = df['subway']
    l = []
    for i in subway:
        if i is not np.nan:
            l.append(1)
        else:
            l.append(0)
    subway = pd.Series(l, index=df.index)
    data['subway'] = subway
    # 上架时间间隔计算
    shelf_time = pd.to_datetime(df['shelf_time'].values)
    download_time = pd.to_datetime(df['download_time'].values)
    delta = download_time - shelf_time
    time_list = [delta[i].days for i in range(len(delta))]
    time_delta = pd.Series(time_list, index=df.index)
    data['time_delta'] = time_delta
    #结合探索发现租金，上架时间间隔存在极端值，采取筛选剔除
    data=data[data['rent']<50000]
    data = data[data['time_delta'] < 700]
    print(data)
    # data.to_csv('data/data.csv')
