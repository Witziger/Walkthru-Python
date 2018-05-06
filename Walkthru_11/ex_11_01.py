import re
hand = open('actualdata.txt')
numlist = list ()

for line in hand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if len(x) > 0:
        total = 0
        for num in x:
            value = int(num)
            numlist.append(value)
            total = sum(numlist)
print (total)
