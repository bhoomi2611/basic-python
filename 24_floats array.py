#Create an array of 5 floats and calculate their sum.
array=[]
sum=0
n=int(input("Enter the length of array"))
for i in range(0,n):
    m=float(input())
    array.append(m)
    sum=sum+m
print("average is",sum/len(array))        