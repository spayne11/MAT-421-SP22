# -*- coding: utf-8 -*-
"""mat421.moduleFhw.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S7SxtbdhNx9YwEvukrPejM_voiP2Mycz

Sydney Payne

Spring 2022 - MAT 421

Module F Homework

CH 20: Numerical Differentiation

Using Finite Difference to Approximate Derivatives
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")
# %matplotlib inline

#step size
h=0.1
#define grid
x=np.arange(0,2*np.pi,h)
#compute function
y=np.cos(x)

#compute vector of forward differences
forward_diff=np.diff(y)/h
#compute corresponding grid
x_diff=x[:-1:]
#compute exact solution
exact_solution=-np.sin(x_diff)

#plot solution
plt.figure(figsize=(12,8))
plt.plot(x_diff,forward_diff,"-",\
         label="Finite difference approximation")
plt.plot(x_diff,exact_solution,label="Exact Solution")
plt.legend()
plt.show()

#compute max error between
#numerical derivative and exact solution
max_error=max(abs(exact_solution-forward_diff))
print(max_error)

import numpy as np

#define step size
h1=1
#define number of iterations to perform
iterations=20
#list to store our step size
step_size=[]
#list to store max error for each step size
max_error1=[]

for i in range(iterations):
  #halve the step size
  h1/=2
  #store this step size
  step_size.append(h1)
  #compute new grid
  x1=np.arange(0,2*np.pi,h1)
  #compute function value at grid
  y1=np.cos(x1)
  #compute vector of forward differences
  forward_diff1=np.diff(y1)/h1
  #compute corresponding grid
  x_diff1=x1[:-1]
  #compute exact solution
  exact_solution1=-np.sin(x_diff1)

  #compute max error between
  #numerical derivative and exact solution
  max_error1.append(max(abs(exact_solution1-forward_diff1)))

#produce log-log plot of max error versus step size
plt.figure(figsize=(12,8))
plt.loglog(step_size,max_error1,"v")
plt.show()

"""    Numerical Differentiation with Noise"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")
# %matplotlib inline

x2=np.arange(0,2*np.pi,0.01)
#compute function
omega=100
epsilon=0.01

y2=np.cos(x2)
y_noise2=y2+epsilon*np.sin(omega*x2)

#plot solution
plt.figure(figsize=(12,8))
plt.plot(x2,y_noise2,"r-",label="cos(x2)+noise")
plt.plot(x2,y2,"b-",label="cos(x2)")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()

x3=np.arange(0,2*np.pi,0.01)
#compute function
y3=-np.sin(x3)
y_noise3=y3+epsilon*omega*np.cos(omega*x3)

#plot solution
plt.figure(figsize=(12,8))
plt.plot(x3,y_noise3,"r-",label="Derivative cos(x3)+noise")
plt.plot(x3,y3,"b-",label="Derivative of cos(x3)")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()

"""End of Chapter Questions

1
"""

import numpy as np
import matplotlib.pyplot as plt

def my_der_calc(f,a,b,N,option):
  n=N
  x4=np.inspace(a,b,n)
  if option == "forward":
    X4=x4[0:n-1]
    df4=(f(x4[1:n]-f(x4[0:n-1]))/(x4[1:n]-x4[0:n-1])
  elif option == "backward":
    X4=x4[1:0]
    df4=(f(x4[1:n])-f(x4[0:n-1]))/(x4[1:n]-x4[0:n-1])
  else:
    X4=x4[1:n-1]
    df=(f(x4[2:n])-f(x4[0:n-2]))/(x4[2:n]-x4[0:n-2])
  return df,X4

def plot_graph(df,X4):
  plt.figure(figsize=(12,8))
  plt.plot(x4,np.cos(x4),label="analytic")
  plt.plot(X4,df,label="forward")
  plt.plot(X4,df,label="backward")
  plt.plot(X4,df,label="central")
  plt.legend()
  plt.title("Analytic and Numerical Derivatives of Sine")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.show()
  x4=np.linspace(0,2*np.pi,100)
  f=lambda x4:np.sin(x4)
  print("Enter Values:\n 1.forward\n 2.backwards\n 3.central\n")
  option=input()
  if option == "forward":
    [df,X4]=my_der_calc(f,0,2*np.pi,10,"forward")
    plot.graph(df,X4)
  elif option == "backward":
    [df,X4]=my_der_calc(f,0,2*np.pi,10,"backward")
    plot_graph(df,X4)
  elif option == "central":
    [df,X4]=my_der_calc(f,0,2*np.pi,10,"central")
    plot_graph(df,X4)
  else:
    print("Check the entered values, by default central.")
    exit(1)

"""    2."""

import numpy as np
import matplotlib.pyplot as plt

def my_num_diff(f2,a2,b2,n2,option2):
  x5=np.linspace(a2,b2,n2)
  if option2 == "forward":
    xf5=x5[0:n2-1]
    dyf=(f2(x5[1:n2])-f2(x5[0:n2-1]))/(x5[1:n2]-x5[0:n2-1])
    return dyf,xf5
  elif option2 == "backward":
    xb2=x5[1:n2]
    dyb=(f2(x5[1:n2])-f2(x5[0:n2-1]))/(x5[1:n2]-x5[0:n2-1])
    return dyb, xb2
  else:
    xc2=x5[1:n2-1]
    dyc=(f2(x5[2:n2])-f2(x5[0:n2-2]))/(x5[2:n2]-x5[0:n2-2])
    return dyc,xc2
x5=np.linspace(0,2*np.pi,100)
f2=lambda x5: np.sin(x5)
[dyf,xf5]=my_num_diff(f2,0,2*np.pi,10,"forward")
[dyb,xb2]=my_num_diff(f2,0,2*np.pi,10,"backward")
[dyc,xc2]=my_num_diff(f2,0,2*np.pi,10,"central")

plt.figure(figsize=(12,8))
plt.plot(x5,np.cos(x5),label="analytic")
plt.plot(xf5,dyf,label="forward")
plt.plot(xb2,dyb,label="backward")
plt.plot(xc2,dyc,label="central")
plt.legend()
plt.title("Analytic and Numerical Derivatives of Sine")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def my_num_diff2(f3,a3,b3,n3,option3):
  x6=np.linspace(a3,b3,n3)
  if option3 == "central":
    xc3=x6[2:n3-1]
    dyc3=(f3(x6[2:n3])-f3(x6[0:n3-2]))/(x6[2:n3]-x6[0:n3-2])
    return dyc3,xc3

x6=np.linspace(0,np.pi,1000)
f3=lambda x6: np.sin(np.exp(x6))
[dy10,X10]=my_num_diff2(f3,0,np.pi,10,"central")
[dy20,X20]=my_num_diff2(f3,0,np.pi,20,"central")
[dy30,X30]=my_num_diff2(f3,0,np.pi,30,"central")

plt.figure(figsize=(12,8))
plt.plot(x6,np.cos(np.exp(x6)),label="analytic")
plt.plot(X10,dy10,label="10 points")
plt.plot(X20,dy20,label="20 points")
plt.plot(X30,dy30,label="30 points")
plt.legend()
plt.title("Analytic and Numerical Derivatives of Sine")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

"""    3."""

import numpy as np

def my_num_diff_w_smoothing(x7,y7,n7):
  x_smooth=x7[np.arange(n7,len(x7)-n7,n7)];
  def smoothData(x7,y7,n7):
    from numpy.lib.function_base import average
    discrete=np.arange(n7 +1,len(y7)-n7,n7)
    s=[]
    for k in range(0,len(discrete)):
      i=discrete[k]
      s.append(average(y7[np.arange(i-n7-1,i+n7)]));
    return np.array(s)
  def central_difference(y7,h7):
    dy7=[]
    for i in range(1,len(y7)-1):
      dy7.append((y7[i+1]-y7[i-1])/(2*h7));
    return np.array(dy7)
  y_smooth=smoothData(x7,y7,n7)
  x71=x_smooth[np.arange(1,len(x_smooth)-1)]
  h7=(x71[len(x71)-1]-x71[0])/(len(x71)-1);
  dy7=central_difference(y_smooth,h7);
  
  return (dy7,x71)

import numpy as np
import matplotlib.pyplot as plt

x7=np.linspace(0,2*np.pi,100)
y7=np.sin(x7)+np.random.randn(len(x7))/100
[dy7,x71]=my_num_diff_w_smoothing(x7,y7,4)

plt.figure(figsize=(12,12))
plt.subplot(211)
plt.plot(x7,y7)
plt.title("Noisy Sine Function")
plt.xlabel("x")
plt.ylabel("y")
plt.subplot(212)
plt.plot(x7,np.cos(x7),"b",label="cosine")
plt.plot(x7[:-1],(y7[1:]-y7[:-1])/(x7[1]-x7[0]),"g",label="unsmoothed forward diff")
plt.plot(x71,dy7,"r",label="smoothed")
plt.title("Analytic Derivatives and Smoothed Derivatives")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.tight_layout()
plt.show()