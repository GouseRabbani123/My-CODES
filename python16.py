#program to find out a string is palindrome or not?

a = input()
b = a[::-1]
print(b)
if(a==b):
    print("This string is palindromee")
else:
    print("This is not a palindrome")


#Another way to find out the palindrome

a = input()
rev = ""
for ch in a:
    rev = ch + rev
if(rev == a):
    print("This string is palindromee")
else:
    print("This is not a palindrome")
  




