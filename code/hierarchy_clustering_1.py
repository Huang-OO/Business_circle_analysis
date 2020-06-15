#谱系聚类图
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage,dendrogram

#参数初始化
readfile = '../data/standardized.xls' #标准化后的数据文件
data = pd.read_excel(readfile, index_col = u'基站编号') #读取数据

#这里使用scipy的层次聚类函数
Z = linkage(data, method = 'single', metric = 'euclidean') #谱系聚类图
P = dendrogram(Z, 0) #画谱系聚类图
plt.show()