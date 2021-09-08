# Write a program to reverse a String
str1=input("Enter the string: ")
arr=""
l=len(str1)
while(l):
    arr+=str1[l-1]
    l=l-1
print("reversed string is",arr)