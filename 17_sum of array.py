#Write a Java program to sum values of an array
array=[]
sum=0
n=int(input("enter length of array"))
for i in range(0,n):
    m=int(input())
    array.append(m)
    sum=sum+m
print(sum)    