# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input('Enter count:'))
position = int(input('Enter position: '))
tags_lst = []

while count > 0:
    tags = soup('a')
    tags_18 = tags[position-1]
    needed_tag = tags_18.get('href', None)
    tags_lst.append(needed_tag)
    url = str(needed_tag)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print ('Retrieving: ', url)
    count = count - 1


#寫迴圈，進第18項，讀取，變list，再度讀第18項
