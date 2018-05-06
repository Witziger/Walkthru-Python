import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter - ')
uh = urllib.request.urlopen(url)
data = uh.read()

print('Retrieving', url)
print('Retrieved', len(data), 'characters')
#extract Json


info = json.loads(data)
comment = info ['comments']
print('count:', len(comment))

numlist = list()
for item in comment:
    num = item['count']
    value = int(num)
    numlist.append(value)
    total = sum(numlist)
print(total)
