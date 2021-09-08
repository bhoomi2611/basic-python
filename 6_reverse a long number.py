#Write a Java program to get a long number as input and reverse the number
n=int(input())
new=0
while(n):
    i=n%10
    new=new*10+i
    n=n//10
print(new)    