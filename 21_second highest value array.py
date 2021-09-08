#Input values to an array from the user and sort the array in ascending order.
arr=[]
n=int(input("length of array:"))
for j in range(0,n):
    m=int(input())
    arr.append(m)
for i in range(0,n):
    for j in range(i+1,n):    
        if(arr[i] < arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
print("second highest element",arr[1])               
