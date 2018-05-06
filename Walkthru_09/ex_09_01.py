name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if not line.startswith("From ") : continue
    line = line.rstrip()
    email = line.split()
    email = email[1]

#2018-03-22卡在這邊，問題出在命名“emails” 誤導自己

    counts[email] = counts.get(email,0) + 1

#print(counts)

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print (bigword, bigcount)
