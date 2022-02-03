n = int(input())
arr =  []
for i in range(n):
    s = input().split()
    for j in range(1,len(s)):
        s[j] = int(s[j])
        if s[0] == "insert":
            arr.insert(s[1],s[2])
            print(arr)
        elif s[0] == "insert":
            arr.insert(s[1],s[2])
            print(arr)
            #example insert works like this
            # fruits = ['apple', 'banana', 'cherry']
            # fruits.insert(1, "orange") 
            # print(fruits)
            # output = ['apple', 'orange', 'banana', 'cherry']
        elif s[0] == "remove":
            arr.remove(s[1])
            #example remove works like this
            # fruits = ['apple', 'banana', 'cherry']
            # fruits.remove("banana")
            # print(fruits)
            # output:['apple', 'cherry']
        elif s[0] == "pop":
            arr.pop(s[1])
            # example:#The pop() method removes the element at the specified position.
            # fruits = ['apple', 'banana', 'cherry']
            # fruits.pop(1)
            # print(fruits)
            # output:['apple', 'cherry']
        elif s[0] == "sort":
            arr.sort()
            #example:The sort() method sorts the list ascending by default.
            # cars = ['Ford', 'BMW', 'Volvo']
            # cars.sort()
            # print(cars)
            # output:['BMW', 'Ford', 'Volvo']
        elif s[0] == "reverse":
            arr.reverse()
            #exaample:The reverse() method reverses the sorting order of the elements.
            # fruits = ['apple', 'banana', 'cherry']
            # fruits.reverse()
            # print(fruits)
            #output:['cherry', 'banana', 'apple']
        elif s[0] == "print":
            print(arr)

            
            
            
            
            
            
            
            
            
            
            
            
            