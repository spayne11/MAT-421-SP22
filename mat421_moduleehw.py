# -*- coding: utf-8 -*-
"""mat421.moduleEhw.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n-UUVuHW6osonM6MvQeoqDD-X9RmZ6Fc

Sydney Payne

Spring 2022 - MAT 421

Module E Homework

Limits
"""

from sympy import *
x=Symbol('x')
expr=sin(x)/x;
print("Expression:{}".format(expr))
limit_expr=limit(expr,x,0)
print("Limit of the expression tends to 0:{}".format(limit_expr))

expr2=3/(2*x-4)
print("Expression:{}".format(expr2))
limit_expr2=limit(expr2,x,2)
print("Limit of the expression tend to 2:{}".format(limit_expr2))

"""Differentiation


    Single Variable

"""

from sympy import *
x=Symbol('x')
f=x**2
derivative_f=f.diff(x)

derivative_f

f1=2*x**5
f1.diff(x)

f2=3/(2*x-4)
f2.diff(x)

"""    Multi-Variable"""

y=Symbol('y')
f3=4*y**8+5*x**2
f3.diff(x)

f3.diff(y)

f4=5*(x**84)*(y**6)
f4.diff(x)

f4.diff(y)

"""Taylor's Series

    Approximations using Taylor Series
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")

x1=np.linspace(-np.pi,np.pi,200)
y1=np.zeros(len(x1))

labels=["First Order","Third Order","Fifth Order","Seventh Order"]
plt.figure(figsize=(10,8))
for n, label in zip(range(4),labels):
  y1=y1+((-1)**n*(x1)**(2*n+1))/np.math.factorial(2*n+1)
  plt.plot(x1,y1,label=label)

  plt.plot(x1,np.sin(x1),"k",label="Analytic")
  plt.grid()
  plt.title("Taylor Series Approximations of Various Orders")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.legend()
  plt.show()

x2=np.pi/2
y2=0
for n in range(4):
  y2=y2+((-1)**n*(x2)**(2*n+1))/np.math.factorial(2*n+1)
print(y2)

x3=np.linspace(0,3,30)
y3=np.exp(x3)

plt.figure(figsize=(14,4.5))
plt.subplot(1,3,1)
plt.plot(x3,y3)
plt.grid()
plt.subplot(1,3,2)
plt.plot(x3,y3)
plt.grid()
plt.xlim(1.7,2.3)
plt.ylim(5,10)
plt.subplot(1,3,3)
plt.plot(x3,y3)
plt.grid()
plt.xlim(1.92,2.08)
plt.ylim(6.6,8.2)
plt.tight_layout()
plt.show()

np.exp(1)

np.exp(0.01)

"""    Truncation Errors for Taylor Series"""

import numpy as np

exp=0
x4=2
for i in range(10):
  exp=exp+(x4**i)/np.math.factorial(i)
  print(f"Using {i}-term,{exp}")
  print(f"The true e^2 is:\n{np.exp(2)}")

"""    Estimating Truncation Errors"""

abs(7.3887125220458545-np.exp(2))

"""    Round-off Errors for Taylor Series"""

exp=0
x5=-30
for i in range(200):
  exp=exp+(x5**i)/np.math.factorial(i)
print(f"Using {i}-term, our result is {exp}")
print(f"The true e^2 is: {np.exp(x5)}")

"""Optimization"""

import numpy as np
from scipy.optimize import minimize

def rosen(x):

  x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
  res = minimize(rosen, x0, method='nelder-mead')

  print(res.x)

"""Logistic Regression"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt

candidates = {'gmat': [780,750,690,710,680,730,690,720,740,690,610,690,710,680,770,610,580,650,540,590,620,600,550,550,570,670,660,580,650,660,640,620,660,660,680,650,670,580,590,690],
              'gpa': [4,3.9,3.3,3.7,3.9,3.7,2.3,3.3,3.3,1.7,2.7,3.7,3.7,3.3,3.3,3,2.7,3.7,2.7,2.3,3.3,2,2.3,2.7,3,3.3,3.7,2.3,3.7,3.3,3,2.7,4,3.3,3.3,2.3,2.7,3.3,1.7,3.7],
              'work_experience': [3,4,3,5,4,6,1,4,5,1,3,5,6,4,3,1,4,6,2,3,2,1,4,1,2,6,4,2,6,5,1,2,4,6,5,1,2,1,4,5],
              'admitted': [1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1]
              }

df = pd.DataFrame(candidates,columns= ['gmat', 'gpa','work_experience','admitted'])

#print (df)

X = df[['gmat', 'gpa','work_experience']]
y = df['admitted']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)

logistic_regression= LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)

confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)

print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

candidates = {'gmat': [780,750,690,710,680,730,690,720,740,690,610,690,710,680,770,610,580,650,540,590,620,600,550,550,570,670,660,580,650,660,640,620,660,660,680,650,670,580,590,690],
              'gpa': [4,3.9,3.3,3.7,3.9,3.7,2.3,3.3,3.3,1.7,2.7,3.7,3.7,3.3,3.3,3,2.7,3.7,2.7,2.3,3.3,2,2.3,2.7,3,3.3,3.7,2.3,3.7,3.3,3,2.7,4,3.3,3.3,2.3,2.7,3.3,1.7,3.7],
              'work_experience': [3,4,3,5,4,6,1,4,5,1,3,5,6,4,3,1,4,6,2,3,2,1,4,1,2,6,4,2,6,5,1,2,4,6,5,1,2,1,4,5],
              'admitted': [1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1]
              }

df = pd.DataFrame(candidates,columns= ['gmat', 'gpa','work_experience','admitted'])

X = df[['gmat', 'gpa','work_experience']]
y = df['admitted']  

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)  #train is based on 75% of the dataset, test is based on 25% of dataset

logistic_regression= LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)

print (X_test) #test dataset
print (y_pred) #predicted values

"""K-means"""

from sklearn.cluster import KMeans
import numpy as np
X7 = np.array([[1, 2], [1, 4], [1, 0],[10, 2], [10, 4], [10, 0]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
kmeans.labels_
kmeans.predict([[0, 0], [12, 3]])
kmeans.cluster_centers_

"""Vector Machine"""

from sklearn import svm
X7 = [[0, 0], [1, 1]]
y7 = [0, 1]
clf = svm.SVC()
clf.fit(X7, y7)

clf.predict([[2., 2.]])

clf.support_vectors_

clf.support_vectors_

clf.n_support_

X8 = [[0], [1], [2], [3]]
Y8 = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X8, Y8)

dec = clf.decision_function([[1]])
dec.shape[1]

clf.decision_function_shape = "ovr"
dec = clf.decision_function([[1]])
dec.shape[1]

lin_clf = svm.LinearSVC()
lin_clf.fit(X8, Y8)

dec = lin_clf.decision_function([[1]])
dec.shape[1]

from sklearn import svm
X9 = [[0, 0], [2, 2]]
y9 = [0.5, 2.5]
regr = svm.SVR()
regr.fit(X9, y9)

regr.predict([[1, 1]])

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

clf = make_pipeline(StandardScaler(), SVC())

linear_svc = svm.SVC(kernel='linear')
linear_svc.kernel

rbf_svc = svm.SVC(kernel='rbf')
rbf_svc.kernel

import numpy as np
from sklearn import svm
def my_kernel(X10, Y10):
    return np.dot(X10, Y10.T)

clf = svm.SVC(kernel=my_kernel)

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn import svm
X11, y11 = make_classification(n_samples=10, random_state=0)
X_train , X_test , y_train, y_test = train_test_split(X, y, random_state=0)
clf = svm.SVC(kernel='precomputed')
gram_train = np.dot(X_train, X_train.T)
clf.fit(gram_train, y_train)

gram_test = np.dot(X_test, X_train.T)
clf.predict(gram_test)

"""Mathematical Formulation"""

import math
math.pi

r=3
circumference=2*math.pi*r
f"Circumference of a Circle =2*{math.pi:.4}*{r}={circumference:.4}"

r2 = 5
area = math.pi * r2 * r2
f"Area of a Circle = {math.pi:.4} * {r2} * {r2} = {area:.4}"

f"Positive Infinity = {math.inf}"

f"Negative Infinity = {-math.inf}"

"""Activation Functions"""

import numpy as np
import matplotlib.pyplot as plt
import numpy as np

def binaryStep(x):
    ''' It returns '0' is the input is less then zero otherwise it returns one '''
    return np.heaviside(x,1)

x12 = np.linspace(-10, 10)
plt.plot(x12, binaryStep(x12))
plt.axis('tight')
plt.title('Activation Function :binaryStep')
plt.show()

def linear(x):
    ''' y = f(x) It returns the input as it is'''
    return x

x13 = np.linspace(-10, 10)
plt.plot(x13, linear(x13))
plt.axis('tight')
plt.title('Activation Function :Linear')
plt.show()

def sigmoid(x):
    ''' It returns 1/(1+exp(-x)). where the values lies between zero and one '''

    return 1/(1+np.exp(-x))

x14 = np.linspace(-10, 10)
plt.plot(x14, sigmoid(x14))
plt.axis('tight')
plt.title('Activation Function :Sigmoid')
plt.show()

def tanh(x):
    ''' It returns the value (1-exp(-2x))/(1+exp(-2x)) and the value returned will be lies in between -1 to 1.'''

    return np.tanh(x)

x15 = np.linspace(-10, 10)
plt.plot(x15, tanh(x15))
plt.axis('tight')
plt.title('Activation Function :Tanh')
plt.show()

def RELU(x):
    ''' It returns zero if the input is less than zero otherwise it returns the given input. '''
    x1=[]
    for i in x:
        if i<0:
            x1.append(0)
        else:
            x1.append(i)

    return x1

x16 = np.linspace(-10, 10)
plt.plot(x16, RELU(x16))
plt.axis('tight')
plt.title('Activation Function :RELU')
plt.show()

def softmax(x):
    ''' Compute softmax values for each sets of scores in x. '''
    return np.exp(x) / np.sum(np.exp(x), axis=0)

x17 = np.linspace(-10, 10)
plt.plot(x17, softmax(x17))
plt.axis('tight')
plt.title('Activation Function :Softmax')
plt.show()

"""Cost Function"""

# importing libraries
#for versions checkout requirements.txt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing and reading data sets
data = pd.read_csv("bmi_and_life.csv")

#look at top 5 rows in data set
data.head()



#delete/drop 'Country' variable.
data = data.drop(['Country'], axis = 1)


#reading into variables
X18 = data.iloc[:, :-1].values
Y18 = data.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X18_train,X18_test,y18_train,y18_test = train_test_split(X18,Y18, test_size = 20, random_state = 0)

#import linear regression
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

#fitting the model
lr.fit(X18_train,y18_train)
LinearRegression(copy_X18=True, fit_intercept=True, n_jobs=1, normalize=False)

# Predicting the Test set results
y18_pred = lr.predict(X18_test)

