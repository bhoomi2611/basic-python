# Program to find duplicate elements in an String array.
arr=[]
count=0
n=int(input("length of array:"))
for j in range(0,n):
    m=input()
    arr.append(m)
for i in range(0,n):
    for j in range(i+1,n/2):
        if(arr[j]==arr[i]):
            print("duplicate term",arr[i])
            count=count+1
print(count)            
            


