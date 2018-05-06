#Python 中有一個內建的功能叫做socket，它用來連接網絡，和追溯Python program中的資料


import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    mystring = data.decode()
    print(mystring)
mysock.close()


print (ord('H'))
print (ord('e'))
print (ord('l'))
print (ord('o'))


import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen ('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print (counts)



import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen ('https://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())



import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen ('https://unitzwei.wordpress.com/2015/06/28/%E5%9C%A8%E6%9F%8F%E5%85%8B%E8%90%8A%E5%94%B8%E6%94%9D%E5%BD%B1-%E7%8C%B6%E8%B1%AB%E9%81%8E%E5%8D%BB%E5%BE%9E%E6%B2%92%E5%BE%8C%E6%82%94%E9%81%8E/')
for line in fhand:
    print(line.decode().strip())
