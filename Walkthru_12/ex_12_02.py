import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')



#Retrieve all of the anchor tags
tags = soup('span')
numlist = list()
for tag in tags:
    comments = tag.contents
    for num in comments:
        value = int(num)
        numlist.append(value)
        total = sum(numlist)
print(total)
