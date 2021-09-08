#Define a method to find out if the number is prime or not.
n=int(input("enter your number"))
if(n>1):
    for r in (2,(n/2)+1):
        if(n%r==0):
           print("not prime")
           break
    else:
        print("prime")
else:
    print("not prime")            
        
