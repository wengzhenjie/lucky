#聚类结果分析
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df=pd.read_csv('data/cls_data.csv',index_col=0)
    print(df['cls_result'].value_counts())
    # # 区域与聚类结果交叉表
    area_cls = pd.crosstab(df['area'], df['cls_result'])
    print(area_cls)
    # # 户型与聚类结果交叉表
    house_type_cls = pd.crosstab(df['house_type'], df['cls_result'])
    print(house_type_cls)
    # # 楼层与聚类结果交叉表
    floor_cls = pd.crosstab(df['floor'], df['cls_result'])
    print(floor_cls)
    # # 有无地铁与聚类结果交叉表
    subway_cls = pd.crosstab(df['subway'], df['cls_result'])
    print(subway_cls)
    #按面积、租金对聚类结果可视化
    for i in range(4):
        # print(df[df['cls_result']==i])
        dfi=df[df['cls_result']==i]
        plt.scatter(dfi['square'], dfi['rent'],label=str(i))
    plt.legend(loc=0, ncol=1)
    plt.show()









