#write a program which will find all such numbers which are divisible by 7 but are not a multiplication of 5 between 2000 and 3200(both included)
#the numbers obtained should be stored in a list?

#Cde start here
res = []
for i in range(2000,3200):
    if(i%7== 0 and i%5!=0):
        res.append(i)
print(res)

#Code end here


#Question 2
#write a program which will have a list of values and then input a number andd check if the value is preent in the list or not and if present how many times?

#Code start here 

lst = [1,2,3,4,1,2,3,1,5,6]
num = int(input("enter a number"))
if num in lst:
    print("the  number is in list",lst.count(num),num) 
else:
    print("not find", num)
    






