nums = [2, 45, 68, 3, 9, 345]
print (max(nums))
print (len(nums))
print (min(nums))
print (sum(nums))

#算平均的做法1

total = 0
count = 0
while True:
    inp = input("Enter a number: ")
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print ("Average: ", average)


#算平均的做法2

numlist = list ()
while True:
    inp = input("Enter a number: ")
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print ("Average: ", average)

#兩種作法的差別在於，作法1 使用的記憶體較少，一次記一個；作法2需要將所有的數字記在記憶體，才能開始計算
#但如果你的資料已經存在一個list,那作法2比較快，因為不需要再寫loop去計算
