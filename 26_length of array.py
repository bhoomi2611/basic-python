#Write a program to find the length of the string "refrigerator".
array=[]
len=0
n=int(input("Enter the length of array"))
for i in range(0,n):
    m=int(input())
    array.append(m)
for k in array:
    len=len+1
print("length is",len)    
