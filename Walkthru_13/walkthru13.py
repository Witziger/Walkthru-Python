import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter - ')
uh = urllib.request.urlopen(url)
data = uh.read()

print('Retrieving', url)
print('Retrieved', len(data), 'characters')
#extract XML
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
print('count: ', len(counts))
numlist = list()
for item in counts:
    num = item.find('count').text
    value = int(num)
    numlist.append(value)
    total = sum(numlist)
print ('Sum: ', total)
#print('Count', item.find('count').text)
