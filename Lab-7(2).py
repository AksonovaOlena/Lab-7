from numpy.fft import fftfreq
import requests
from bs4 import BeautifulSoup
import pylab
r=requests.get('https://www.thecoolist.com/beautiful-cats/')
page=BeautifulSoup(r.text,'html.parser')
print(r.status_code)
row1=page.head.title.text
row2=page.body.text
letters_str='abcdefghijklmnopqrstuvwxyz'
letters=list(letters_str)
frequency=[]
l=len(letters)
for i in range(l):
    elem=letters[i]
    fr=row2.count(elem)
    frequency.append(fr)
xdata=letters
ydata=frequency
pylab.bar(xdata,ydata)
pylab.show()