#聚类分析
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.externals import joblib

#基本配置
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
if __name__ == '__main__':
    df=pd.read_csv('data/data.csv',index_col=0)
    #选择数值型变量租金(rent)、面积(square)、上架时间间隔(time_delta)分析
    cls_values=df[['rent','square','time_delta']].values
    #k值选择  根据SSE趋势选择4
    SSE=[]
    for k in range(1,10):
        clf=KMeans(n_clusters=k,random_state=1234).fit(cls_values)
        SSE.append(clf.inertia_)
    print(SSE)
    plt.plot([i for i in range(1,10)],SSE)
    plt.xlabel("聚类个数")
    plt.ylabel("SSE")
    plt.title("k值选择")
    plt.show()
    clf = KMeans(n_clusters=4,random_state=1234).fit(cls_values)
    # joblib.dump(clf,'model/cls_model.m')
    print(clf.cluster_centers_)
    # [[ 3918.60096154    72.89774859    54.47678236]
    #  [13626.01916431   132.40182218    69.71190701]
    #  [21248.48617788   179.64963942    97.20552885]
    #  [ 7756.37114923    96.8544549     53.36081904]]
    # df['cls_result']=clf.predict(cls_values)
    # df.to_csv('cls_data.csv')
