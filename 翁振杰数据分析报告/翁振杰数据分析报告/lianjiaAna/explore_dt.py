#数据分布探索
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
#基本配置
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
#房源区域分布分析
def ana_area_dt(area_dt):
    plt.bar(area_dt.index,area_dt.values)
    plt.title('房源区域分布情况')
    for x, y in enumerate(area_dt.values):
        plt.text(x - 0.3, y + 90, "%s" % y)
    plt.ylabel('数量')
    plt.xlabel('区域')
    plt.legend(['数量'], loc='upper right')
    plt.show()
#户型分布分析
def ana_house_type_dt(house_type_dt):
    plt.bar(house_type_dt.index, house_type_dt.values)
    plt.title('户型分布情况')
    for x, y in enumerate(house_type_dt.values):
        plt.text(x - 0.3, y + 90, "%s" % y)
    plt.xticks(rotation=90)
    plt.ylabel('数量')
    plt.xlabel('户型')
    plt.legend(['数量'], loc='upper right')
    plt.show()
#楼层分布分析
def ana_floor_dt(floor_dt):
    plt.bar(floor_dt.index, floor_dt.values)
    plt.title('楼层分布情况')
    for x, y in enumerate(floor_dt.values):
        plt.text(x - 0.3, y + 90, "%s" % y)
    plt.xticks(rotation=90)
    plt.ylabel('数量')
    plt.xlabel('楼层')
    plt.legend(['数量'], loc='upper right')
    plt.show()
#面积分布分析
def ana_square_dt(a,square_dt):
    plt.bar(a, square_dt.values)
    plt.title('房源面积分布情况')
    for x, y in enumerate(square_dt.values):
        plt.text(x + 0.7, y + 90, "%s" % y)
    plt.ylabel('数量')
    plt.xticks(a,[str(i)+'-'+str(i+50) for i in range(0,max(square_dt.values),50)],rotation=90)
    plt.xlabel('面积(㎡)')
    plt.legend(['数量'], loc='upper right')
    plt.show()
#租金分布分析
def ana_rent_dt(a,rent_dt):
    plt.bar(a, rent_dt)
    plt.title('租金分布情况')
    for x, y in enumerate(rent_dt):
        plt.text(x + 0.6, y + 30, "%s" % y)
    plt.ylabel('数量')
    xlabels=[str(i) + '-' + str(i + 500) for i in range(0, 25000, 500)]
    xlabels.append('大于25000')
    plt.xticks(a,xlabels , rotation=90)
    plt.xlabel('租金(元)')
    plt.legend(['数量'], loc='upper right')
    plt.show()
#最近地铁距离分布分析
def ana_subway_dt(a,subway_dt):
    plt.bar(a, subway_dt.values)
    plt.title('最近地铁距离分布情况')
    for x, y in enumerate(subway_dt.values):
        plt.text(x + 0.9, y + 30, "%s" % y)
    plt.ylabel('数量')
    plt.xticks(a,[str(i)+'-'+str(i+100) for i in range(0,1200,100)],rotation=90)
    plt.xlabel('最近地铁距离(m)')
    plt.legend(['数量'], loc='upper right')
    plt.show()
# 上架时间分布分析
def ana_time_delta_dt(a,time_delta_dt):
    plt.bar(a, time_delta_dt.values)
    plt.title('上架时间分布情况(截止2019年7月22日)')
    for x, y in enumerate(time_delta_dt.values):
        plt.text(x + 0.9, y + 30, "%s" % y)
    plt.ylabel('数量')
    plt.xticks(a,[str(i)+'-'+str(i+50) for i in range(0,500,50)],rotation=90)
    plt.xlabel('间隔天数(天)')
    plt.legend(['数量'], loc='upper right')
    plt.show()
if __name__ == '__main__':
    df = pd.read_csv('data/info.csv')
    #区域
    area = df['area']
    area_dt=area.value_counts()
    ana_area_dt(area_dt)
    #面积
    square=df['square']
    square=[int(i[:-1]) for i in square.values]
    bins=[i for i in range(0,max(square),50)]
    square=pd.cut(square,bins)
    square_dt = square.value_counts()
    a = [i for i in range(1, 17)]
    ana_square_dt(a,square_dt)
    #租金
    rent=df['rent']
    rent=[int(i) for i in rent.values]
    bins = [i for i in range(0, max(rent), 500)]
    rent=pd.cut(rent, bins)
    rent_dt=rent.value_counts()
    r=rent_dt.values[:50]
    r=np.append(r,sum(rent_dt.values[50:]))
    a = [i for i in range(1, 52)]
    ana_rent_dt(a, r)
    # 户型
    house_type = df['house_type']
    house_type_dt = house_type.value_counts()
    print(len(house_type_dt))
    l1 = house_type_dt[:16]
    l2 = sum(house_type_dt[16:])
    l1['其他户型'] = l2
    house_type_dt = l1
    ana_house_type_dt(house_type_dt)
    # 楼层
    floor = df['floor'].values
    print(len(df['floor'].value_counts()))
    floor = pd.Series([i.split('/')[0] for i in floor])  # 预处理
    floor = floor.value_counts()
    # 进一步处理，将楼层分为低楼层、中楼层、高楼层、未知（未明确楼层，也也归入未知）四种
    floor['未知'] = floor['未知'] + sum(floor[-3:])
    floor_dt = floor[:-3]
    ana_floor_dt(floor_dt)
    #地铁最近距离
    subway=df['subway']
    l=[]
    for i in subway:
        if i is not np.nan:
            r = re.findall('(\d+)m', i)
            v=min([int(i) for i in r])
            l.append(v)
        else:
            l.append(0)
    subway=pd.Series(l,index=df.index)
    subway=[int(i) for i in subway.values]
    bins = [i for i in range(0, 1300, 100)]
    subway=pd.cut(subway, bins)
    subway_dt=subway.value_counts()
    a = [i for i in range(1, 13)]
    ana_subway_dt(a,subway_dt)
    #上架时间分布分析
    shelf_time=pd.to_datetime(df['shelf_time'].values)
    download_time=pd.to_datetime(df['download_time'].values)
    delta=download_time-shelf_time
    time_list=[delta[i].days for i in range(len(delta))]
    time_delta=pd.Series(time_list,index=df.index)
    bins = [i for i in range(0, 550, 50)]
    time_delta=pd.cut(time_delta.values,bins)
    time_delta_dt=time_delta.value_counts()
    a=[i for i in range(1, 11)]
    ana_time_delta_dt(a,time_delta_dt)






