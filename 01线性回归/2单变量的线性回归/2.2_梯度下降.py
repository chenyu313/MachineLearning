import numpy as np

#计算代价函数
#创建一个以参数θ为特征函数的代价函数
def computeCost(X,y,theta):
    #X.dot()表示矩阵点乘
    inner=np.power((X.dot(theta.T)-y),2)
    return np.sum(inner)/(2*len(X))