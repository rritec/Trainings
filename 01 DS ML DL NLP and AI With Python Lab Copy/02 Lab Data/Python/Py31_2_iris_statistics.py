import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('iris.csv')
print(iris.describe()) # summary statistics
print(iris['sepal_length'].count())
print(iris['sepal_width'].count())
print(iris[['sepal_length','sepal_width']].count())
print(type(iris[['sepal_length','sepal_width']].count()))
print(iris['sepal_length'].mean())
print(iris.mean())
print(iris.std())
print(iris.median())
q=0.5
print(iris.quantile(q))
q=[0.25,0.75]
print(iris.quantile(q))
print(iris.min())
print(iris.max())
#draw box plot
iris.plot(kind= 'box')
plt.ylabel('[cm]')
plt.show()