import numpy as np
import pandas as pd
import jieba
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#基本配置
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
if __name__ == '__main__':
    df=pd.read_csv('data/info.csv')
    describe=df['describe']
    #正则去除标点空格等符号以及房源亮点、装修描述、出租原因、交通出行、户型介绍这些无效频繁词，合并后分词，输出txt文件 词云分析
    txt=' '.join(describe.dropna().values)
    inv=["房源亮点","装修描述","出租原因","交通出行","户型介绍"]
    for i in inv:
        txt=txt.replace(i,'')
    r=re.findall(r'\w+',txt)
    word_list=[' '.join(jieba.cut(i)) for i in r]
    text=' '.join(word_list)
    cloud=WordCloud(font_path='C:\windows\Fonts\STKAITI.TTF').generate_from_text(text)
    plt.imshow(cloud)
    plt.show()
    # print(text)



