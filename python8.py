#caluculating the average of  n numbers
print("Calculating Average of n numbers")
n = int(input("How many numbers are there"))
nums = []
sum1 = 0

for i in range(n):
    a = int(input("Enter a number"))
    nums.append(a)
    sum1 = sum1 + nums[i]
print("The sum os all th1
e numbers is", sum1)
avg = sum1/n 
print("The avg of alll the numbers is ",avg)
