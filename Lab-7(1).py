from numpy import *
import matplotlib.pyplot as plt
t=linspace(-2,5)
y=t*sin(5*t)
plt.plot(t,y,'r-',label='t*sin(5*t)')
plt.xlabel('t')
plt.xlabel('y')
plt.title('My first graph in Python')
plt.legend(['t*sin(5*t)'],
        loc='upper left')
plt.show()
