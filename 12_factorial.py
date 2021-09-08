#Write a program to print the factorial of a number.
n=int(input("enter your number: "))
fac=1
while(n):
    fac=fac*n
    n=n-1
print("factorial:",fac)    