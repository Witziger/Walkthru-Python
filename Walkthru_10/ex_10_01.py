name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if not line.startswith("From ") : continue
    line = line.rstrip()
    line = line.split()
    time = line[5]
    hour, minute, second = time.split(':')

    counts[hour] = counts.get(hour,0) + 1

#print (counts)

t = list(counts.items())
t.sort()
for key, val in t:
    print(key, val)
