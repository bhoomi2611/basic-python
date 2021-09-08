# Given an array of integers and a number x, 
# find the smallest sub-array with sum greater than the given value

import math
def subarray(s, arr):
  sum = 0
  l = math.inf
  start = 0

  for last in range(0, len(arr)):
    sum += arr[last]
    while sum >= s:
      l = min(l, last - start + 1)
      sum -= arr[start]
      start += 1
  if l == math.inf:
    return 0
  return l


array=[]
n=int(input("enter length of array"))
sum=0
for i in range(0,n):
    m=int(input())
    array.append(m)
x=int(input("Enter the given sum"))    
v=subarray(x,array)    
print(v)
