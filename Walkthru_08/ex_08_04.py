fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()

s1 = 'But soft what light through yonder window breaks'
s2 = 'It is the east and Juliet is the sun'
s3 = 'Arise fair sun and kill the envious moon'
s4 = 'Who is already sick and pale with grief'

s1 = s1.split()
s2 = s2.split()
s3 = s3.split()
s4 = s4.split()

lst = s1 + s2 + s3 + s4

lst.remove('is')
lst.remove('is')
lst.remove('is')
lst.remove('the')
lst.remove('the')
lst.remove('and')
lst.remove('and')
lst.remove('sun')
lst.append('is')
lst.sort()

print (lst)
