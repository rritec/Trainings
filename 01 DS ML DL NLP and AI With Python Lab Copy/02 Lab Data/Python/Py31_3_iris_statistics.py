import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('iris.csv')
print(iris['species'].describe())
print(iris['species'].unique())
#Filtering by species
indices = iris['species'] == 'setosa'
setosa = iris.loc[indices,:] # extract new DataFrame
indices = iris['species'] == 'versicolor'
versicolor = iris.loc[indices,:] # extract new DataFrame
indices = iris['species'] == 'virginica'
virginica = iris.loc[indices,:] # extract new DataFrame
print(virginica)

print(setosa['species'].unique())
print(versicolor['species'].unique())
print(virginica['species'].unique())
print(setosa.head(2))
print(versicolor.head(2))
print(virginica.head(2))
'''del setosa['species'], versicolor['species'],virginica['species']
print(versicolor['species'].unique())
print(setosa['species'].unique())'''


iris.plot(kind= 'hist', bins=50, range=(0,8), alpha=0.3)
plt.title('Entire iris data set')
plt.xlabel('[cm]')
plt.show()

####################

setosa.plot(kind='hist', bins=50, range=(0,8), alpha=0.3)
plt.title('Setosa data set')
plt.xlabel('[cm]')
versicolor.plot(kind='hist', bins=50, range=(0,8), alpha=0.3)
plt.title('Versicolor data set')
plt.xlabel('[cm]')
virginica.plot(kind='hist', bins=50, range=(0,8), alpha=0.3)
plt.title('Virginica data set')
plt.xlabel('[cm]')
plt.show()