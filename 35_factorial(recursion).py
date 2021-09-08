# Write a program where recursion is used to calculate the factorial of a number.
def fac(num):
    if (num==1):
        return num
    else:
        return num*fac(num-1)    
n=int(input("Enter the number"))
print("factorial is ",fac(n))


