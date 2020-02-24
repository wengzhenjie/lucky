#数据相关情况探索
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#基本配置
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == '__main__':
    df=pd.read_csv('data/data.csv')
    # 区域与租金、上架时间
    g=df.groupby('area')['rent']
    area_rent=pd.DataFrame()
    area_rent['mean']=g.mean()
    area_rent['min'] = g.min()
    area_rent['max'] = g.max()
    print(area_rent)
    plt.plot(area_rent.index,area_rent['mean'],label='mean')
    plt.plot(area_rent.index, area_rent['min'], label='min')
    plt.plot(area_rent.index, area_rent['max'], label='max')
    plt.legend(loc=0, ncol=1)
    plt.title("价格-区域趋势图")
    plt.show()

    g=df.groupby('area')['time_delta']
    area_time=pd.DataFrame()
    area_time['mean']=g.mean()
    area_time['min'] = g.min()
    area_time['max'] = g.max()
    print(area_time)
    plt.plot(area_time.index,area_time['mean'],label='mean')
    plt.plot(area_time.index, area_time['min'], label='min')
    plt.plot(area_time.index, area_time['max'], label='max')
    plt.legend(loc=0, ncol=1)
    plt.title("上架时长-区域趋势图")
    plt.show()

    #户型与租金、上架时间
    g=df.groupby('house_type')['rent']
    house_type_rent=pd.DataFrame()
    house_type_rent['mean']=g.mean()
    house_type_rent['min'] = g.min()
    house_type_rent['max'] = g.max()
    print(house_type_rent)
    plt.plot(house_type_rent.index,house_type_rent['mean'],label='mean')
    plt.plot(house_type_rent.index, house_type_rent['min'], label='min')
    plt.plot(house_type_rent.index, house_type_rent['max'], label='max')
    plt.legend(loc=0, ncol=1)
    plt.xticks(rotation=90)
    plt.title("户型-租金趋势图")
    plt.show()

    g=df.groupby('house_type')['time_delta']
    house_type_time=pd.DataFrame()
    house_type_time['mean']=g.mean()
    house_type_time['min'] = g.min()
    house_type_time['max'] = g.max()
    print(house_type_time)
    plt.plot(house_type_time.index,house_type_time['mean'],label='mean')
    plt.plot(house_type_time.index, house_type_time['min'], label='min')
    plt.plot(house_type_time.index, house_type_time['max'], label='max')
    plt.legend(loc=0, ncol=1)
    plt.xticks(rotation=90)
    plt.title("户型-上架时长趋势图")
    plt.show()

    #户型与面积
    g = df.groupby('house_type')['square']
    house_type_square = pd.DataFrame()
    house_type_square['mean'] = g.mean()
    house_type_square['min'] = g.min()
    house_type_square['max'] = g.max()
    print(house_type_square)
    plt.plot(house_type_square.index, house_type_square['mean'], label='mean')
    plt.plot(house_type_square.index, house_type_square['min'], label='min')
    plt.plot(house_type_square.index, house_type_square['max'], label='max')
    plt.legend(loc=0, ncol=1)
    plt.xticks(rotation=90)
    plt.title("户型-面积")
    plt.show()

    #数据选取,租金(小于5W)、面积、上架时间(小于700)、地铁距离(地铁距离为0不考虑)
    re_sq_ti_su=df[['rent','square','time_delta','subway']]
    re_sq_ti_su = re_sq_ti_su[re_sq_ti_su['rent'] < 50000]
    re_sq_ti_su = re_sq_ti_su[re_sq_ti_su['time_delta'] < 700]
    re_sq_ti_su=re_sq_ti_su[re_sq_ti_su['subway']>0]
    cor = re_sq_ti_su.corr()
    #print(cor)
    #                rent    square  time_delta    subway
    # rent        1.000000  0.649142    0.178392 -0.088873
    # square      0.649142  1.000000    0.279384  0.034736
    # time_delta  0.178392  0.279384    1.000000 -0.006909
    # subway     -0.088873  0.034736   -0.006909  1.000000
    # sns.pairplot(re_sq_ti_su)
    # plt.show()

    #考虑以下
    #基于上面的分析，地铁距离其他因子相关性不是很强，采取二分类措施，将地铁的情况记为01变量，表示地铁有无
    #另一方面剔除极端数据，便于后面分析租金超过5W，上架时间超过700天






