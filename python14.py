#write a program which will inputs 5 names and print the names in Alphabetical order

names = []
for i in range(5):
    a = input("Enter a name")
    names.append(a)
print("These are the given names",names)
names.sort()
print("These are the sorted names",names)



#write a program to input name and marks of 5 students,
#print the name and marks of students who got the highest marks
#and the students who got the lowest marks.

names = []
marks = []
for i in range(5):
    m = input("Enter the name")
    n = int(input("Enter the Marks"))
    names.append(m)
    marks.append(n)
h = max(marks)
l = min(marks)
print("The highest marks of the student is",h)
print("The lowest marks of the students is",l) 

for i in range(5):
    if(h == marks[i]):
        print("thhe student with highest marks is",names[i])
    if(l == marks[i]):
        print("the student with min marks is",names[i])
        
        















 
