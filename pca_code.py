%matplotlib inline
import pandas as pd
import matplotlib.pyploy as plt
import numpy as np
import seaborn as sns

plt.style.use("ggplot") 
plt.rcParams["figure.figsize"] = (12,8)


#using uci iris dataset

https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data 
#this downloads data



iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
, header=None)

iris.head()

#set column names

iris.columns = ["sepal_length", "sepal_width", "petal.length", "petal_width", "species"]
iris.dropna(how='all', inplace=TRUE)
iris.head()


#use seaborn for scatterplot, visually assess if there's good class seperability in dataset 

sns.scatterplot(x = iris.sepal_length, y = iris.sepal_width,    
  hue = iris.species, 
  style = iris.species);

#each species has unique color

#actual steps in PCA here -- standardizing data, zero the mean

#seperate into feature matrix

x = iris. iloc[:,0:4].values
y = iris.species.values

from sklearn.preprocessing import StandardScaler
x = StandardScaler(). fit_transform(x)

#ensures zero mean and unit variance 

#compute eigenvectors & eigenvalues (eigendecomposition)

covariance_matrix = np.cov(x.T)
print("Covariance Matrix : \n", covariance_matrix)

eigen_vectors, eigen_values = np.linalg.eig(covariance_matrix)
print("eigenvalues: \n", eigen_values, "\n")
print("eigenvectors: \n", eigen_vectors)


for val in eigen_values:
  print(val)
  
variance_explain = [(i/sum(eigen_values))*100 for i in eigen_values]

cumulative_var = np.cumsum(variance_explained)
cumulative_var


sns.lineplot(x = [1,2,3,4]
plt.xlabel("number of components")
plt.ylabel("cumulative variance")
plt.title("explain variance ratio")

plt.show()


#select eigenvectors and compute PCA 
eigen_vectors

projection_matrix = (eigen_vectors.T[:][:])[:2].T
print ("projection_matrix :\n", projection_matrix)

X_pca = X.dot(projection_matrix)

for species in ('Iris-setosa','Iris-versicolor', 'Iris-virginica'):
sns.scatterplot(X_pca[y=species,0],
X_pca[y])