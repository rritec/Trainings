import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('iris.csv')
print(iris.shape)
print(iris)
#line chart
iris.plot(x='sepal_length', y='sepal_width')
plt.show()
#scatter chart
iris.plot(x='sepal_length', y='sepal_width',kind='scatter')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()
#box graph
iris.plot(y='sepal_length', kind='box')
plt.ylabel('sepal width (cm)')
plt.show()
#histogram graph
iris.plot(y='sepal_length', kind='hist')
plt.xlabel('sepal length (cm)')
plt.show()
##histogram graph with parameters
iris.plot(y='sepal_length', kind='hist',bins=30, range=(4,8), normed=True)
plt.xlabel('sepal length (cm)')
plt.show()
##histogram graph with parameters
iris.plot(y='sepal_length', kind='hist', bins=30,range=(4,8), cumulative=True, normed=True)
plt.xlabel('sepal length (cm)')
plt.title('Cumulative distribution function (CDF)')
plt.show()
##histogram graph with other syntax
iris.hist('sepal_length')
plt.show()
