#Write a java program to get three numbers as input and print the highest and lowest number
n1=int(input())
n2=int(input())
n3=int(input())
if(n1>=n2 and n1>=n3):
    print("greatest",n1)
    if(n2>=n3):
        print("lowest",n3)
    else:
        print("lowest",n2)
elif(n2>=n3 and n2>=n1):
    print("greatest",n2)
    if(n1>=n3):
        print("lowest",n3)
    else:
        print("lowest",n1)
else:
    print("greatest",n3)
    if(n1>n2):
        print("lowest",n2)
    else:
        print("lowest",n1)                    
