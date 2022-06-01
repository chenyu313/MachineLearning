import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#需要在现有数据集上，训练线性回归的参数θ
#这个部分计算J(Ѳ)，X是矩阵
def computeCost(X,y,theta):
    inner=np.power(((X*theta.T)-y),2)
    return np.sum(inner)/(2*len(X))