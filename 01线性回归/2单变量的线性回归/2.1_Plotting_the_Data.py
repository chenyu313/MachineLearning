import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#读入数据，然后展示数据
path='D:\PycharmProjects\MachineLearning\ML_data\ex1data1.txt'
#读取数据，数据没有标题，自己设置
data=pd.read_csv(path,header=None,names=['Population','Profit'])
#输出表格
print(data.head())
#画图
data.plot(kind='scatter',x='Population',y='Profit',figsize=(12,8))
plt.show()