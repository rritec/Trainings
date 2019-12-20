# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:11:42 2017

@author: snittal2
"""



from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier, RandomForestRegressor, ExtraTreesRegressor
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import neighbors
from sklearn.model_selection import LeaveOneOut, LeavePOut
import numpy as np
from sklearn.metrics import roc_auc_score,mean_squared_error,r2_score
from sklearn.model_selection import LeaveOneGroupOut,GridSearchCV
from sklearn.linear_model import LogisticRegression, Lasso, Ridge, BayesianRidge, SGDClassifier,LassoCV, LinearRegression
from sklearn import svm
from sklearn.feature_selection import RFECV, RFE,SelectFromModel
from sklearn.preprocessing import normalize
from sklearn import tree
from sklearn.neural_network import MLPRegressor, MLPClassifier
from sklearn.decomposition import PCA, KernelPCA,NMF
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import LeaveOneGroupOut,GridSearchCV
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression, Lasso, Ridge, BayesianRidge, SGDClassifier
from sklearn import svm
from sklearn.feature_selection import RFECV, RFE,SelectFromModel
from sklearn.preprocessing import normalize
from sklearn import tree
import random
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import minmax_scale
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
import scipy
import scipy.integrate
from scipy import io
from sklearn.model_selection import train_test_split
import math
import scipy.io as sio
mat_contents = sio.loadmat('610d.mat')

inputs=mat_contents['RPM1']

outputs=mat_contents['HC1']



#inputs=np.append(inputs_1,outputs,axis=1)


inputs=StandardScaler().fit_transform(inputs)


X_train, X_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.30, random_state=42)

rf_pred=np.zeros(np.shape(y_test))
clf=RandomForestRegressor(n_estimators=100)
clf.fit(X_train,y_train)
rf_pred=clf.predict(X_test)
train_pred=clf.predict(X_train)
print(math.sqrt(mean_squared_error(y_test,rf_pred)))

mat_input=np.row_stack((y_train,y_test))
mat_output=np.append(train_pred,rf_pred,axis=0)
mat=np.column_stack((mat_input,mat_output))
scipy.io.savemat('610dRF.mat', mdict={'arr': mat})

rf_pred=np.zeros(np.shape(y_test))
clf=ExtraTreesRegressor(n_estimators=100)
clf.fit(X_train,y_train)
rf_pred=clf.predict(X_test)
train_pred=clf.predict(X_train)
print(math.sqrt(mean_squared_error(y_test,rf_pred)))

mat_input=np.row_stack((y_train,y_test))
mat_output=np.append(train_pred,rf_pred,axis=0)
mat=np.column_stack((mat_input,mat_output))
scipy.io.savemat('610dET.mat', mdict={'arr': mat})

rf_pred=np.zeros(np.shape(y_test))
clf=Lasso(alpha=100)
clf.fit(X_train,y_train)
rf_pred=clf.predict(X_test)
train_pred=clf.predict(X_train)
print(math.sqrt(mean_squared_error(y_test,rf_pred)))

mat_input=np.row_stack((y_train,y_test))
mat_output=np.append(train_pred,rf_pred,axis=0)
mat=np.column_stack((mat_input,mat_output))
scipy.io.savemat('610dLasso.mat', mdict={'arr': mat})

