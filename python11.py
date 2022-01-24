print("Calculating Mode of N numbers ")
n = int(input("How many numbers are there"))
nums = []
for i in range (n):
    a = int(input("Enter a number"))
    nums.append(a)
    
differentNums={}
for x in nums:
    if x not in differentNums:
        differentNums[x]=1
    else:
        differentNums[x]+=1
print("Numbers with their frequency are")
maxFreq = 0
mode = 0
for d in differentNums.keys():
    print(d," Comes",differentNums[d],"timer")
    














