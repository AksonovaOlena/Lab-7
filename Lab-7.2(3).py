from matplotlib.cbook import file_requires_unicode
from matplotlib.pyplot import xscale
import requests
from bs4 import BeautifulSoup
from numpy import *
import matplotlib.pyplot as plt
import pylab
r=requests.get("https://www.k9ofmine.com/most-beautiful-dog-breeds/")
page=BeautifulSoup(r.text,'html.parser')
#print(r.status_code)
row1=page.head.title.text
row2=page.body.text
names=['Крапки','Коми','Знаки питання']
frequency=[0,0,0]
frequency[0]=row2.count('. ')
frequency[1]=row2.count(', ')
frequency[2]=row2.count('? ')
xdata=names
ydata=frequency
#plt.plot(frequency,'r')
pylab.bar(xdata,ydata)
plt.title('Кількість знаків в тексті')
pylab.savefig('sentences.png',dpi=200)
pylab.show()