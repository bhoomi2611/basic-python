#Write a Java Program to find average of an int Array
array=[]
sum=0
n=int(input("Enter the length of array"))
for i in range(0,n):
    m=int(input())
    array.append(m)
    sum=sum+m
print("Average is",sum/len(array))    