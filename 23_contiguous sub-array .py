# Given an integer array, 
# find the contiguous sub-array (containing at least onenumber) which has the largest sum and return its sum
arr=[]
count=0
n=int(input("length of array:"))
for j in range(0,n):
    m=int(input())
    arr.append(m)
      
curr = 0
next = 0
for i in range(0, n):
    next = next + arr[i]
    if next < 0:
        next = 0
    elif (curr < next):
        curr = next
              
print(curr)   