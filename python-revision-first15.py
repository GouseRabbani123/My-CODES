#1. to print the Arm strong number


#for i in range(1001):
i = int(input("Enter  a Number"))
result = 0 
#n = len(str(i)) #As we cant find out thee length of a number  so here we are converting the number in the form of string by using the perticular code.
n = len(str(i))  
#print(n)
while(i != 0):
    #print(i)
    digit = i%10
    #print(digit)
    result = result + digit**n 
    i = i//10
    print(result)
    if(result == i):
        print(i, "is a ArmStrong number")