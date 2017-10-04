import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

address = ' http://py4e-data.dr-chuck.net/known_by_Colton.html'
#html = urllib.request.urlopen(url).read()
totsum = 0
#soup = BeautifulSoup(html, 'html.parser')
n = 0
x = 0
while n < 7:
    html = urllib.request.urlopen(address).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    
    for link in tags:
        x = x + 1
        if x == 18:
            address = link.get('href', None)
            #print (address)
            x = 0
            break
    n = n + 1

print (address)