# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
x = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    data = float(line[20:])
    x = x + data

avg = x/count
print('Average spam confidence: ', avg)

#計算出小數在那行的位置
#data = 'X-DSPAM-Confidence: 0.8475'
#clpos = data.find(':')
