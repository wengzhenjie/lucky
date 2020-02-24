#回归预测
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split,ParameterGrid,GridSearchCV
from sklearn import tree
from sklearn.externals import joblib
from sklearn import tree
import pydotplus
#基本配置
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
df=pd.read_csv('data/reg_data.csv',index_col=0)
rent=df['rent'].values
del df['rent']
del df['time_delta']
X=df.values
#切分数据集
train_data, test_data, tarin_target, test_target = train_test_split(X, rent, test_size=0.2, train_size=0.8,
                                                                    random_state=1234)
if __name__ == '__main__':
    #网格搜索优化
    # param_grid = { 'min_impurity_decrease': np.linspace(0, 0.2, 100),
    #               'max_depth': np.arange(2, 10)}
    # reg = GridSearchCV(tree.DecisionTreeRegressor(random_state=1234), param_grid, cv=5)#5折交叉验证
    # reg.fit(train_data, tarin_target)
    # print("best param:{0}\nbest score:{1}".format(reg.best_params_, reg.best_score_))
    # best param:{'max_depth': 6, 'min_impurity_decrease': 0.0}min_impurity_decrease默认即为0
    # best score:0.9234603688633607
    reg = tree.DecisionTreeRegressor(max_depth=6,random_state=1234)
    reg.fit(train_data, tarin_target)
    # print(reg.score(test_data,test_target))#0.9191105571216933
    # joblib.dump(reg,"model/reg_model.m")
    #决策树可视化
    features=['square', 'subway', 'jingan', 'huangpu', 'zhabei', 'jiading', 'baoshan', 'shanghaizhoubian', 'putuo', 'xuhui', 'changning', 'songjiang', 'chongming', 'fengxian', 'yangpu', 'pudong', 'minhang', 'qingpu', 'jinshan', 'hongkou', 'mid_floor', 'UN_floor', 'high_floor', 'low_floor', '3-2-1', '3-1-1', '2-2-1', '3-1-2', '2-1-2', 'other_type', '4-2-3', '2-2-2', '3-2-3', '1-1-1', '4-2-4', '3-2-2', '1-0-1', '2-0-1', '1-2-1', '4-2-2', '2-1-1', 'cls_result0', 'cls_result1', 'cls_result2', 'cls_result3']
    dot_data = tree.export_graphviz(reg,feature_names=features)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_png('tree.png')
    #预测与实际散点图绘制
    y=reg.predict(X)
    plt.scatter(y,rent)
    plt.plot([0,max(y)],[0,max(y)],color='r')
    plt.title("预测值与实际值对比")
    plt.xlabel("预测值")
    plt.ylabel("实际值")
    plt.show()



# 探索重来
# 论文



