#Lists in Python
# to hold multiple values in a single  variable name we use the lists


#To Change the value in list 
A[0] = 10

#T0 delete the values inthe  list 
del A[0]

#INDEXING AND SCLICING THE LIST 

A = [1,2,3,4,5,6]
print(A[3])( will print 4)
print(A[1:]) will print [2,3,4,5,6]
print(A[1:4]) will print [2,3,4] 
print(A[-2]) will print 5 
print(A[:4]) will print [1,2,3,4] 


#Common list  operations
len(list) used to find the length of the list.
'+' is used for combine two lists ex:[1,2,3] + [4,5,6] will give [1,2,3,4,5,6]
'*' is used to repeat the list elements Eg:['#']*4 will give ['#','#','#','#']
in is used t check  if a value is there in a list or not Eg.3 in [1,2,3,4] will give True and 7 in [1,2,3,4] will give false. 


# How to iterate the list

A = [2,4,6,8,10]

for value in A:
    print(value * value)
will print => 4,16,36,64,100


#Functions used in lists
len(list)
max(list)
min(list)




#Methods with list 
List.append(value)
List.count(value)
List.extend( attaches another list)
List.index(value)

List.insert(index,value)
ex: lst = [1,2,3,4]
    lst.insert(2,50)
    output = lst=>[1,2,50,3,4]
    
 


    
list.remove(value)

List.reverse()

List.sort()

List.pop()



































#Mode of n numbers
a = list(map(int,input().split()))






