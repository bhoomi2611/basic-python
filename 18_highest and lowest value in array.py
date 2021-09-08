#Write a program to find the greatest and lowest value in an array.
def high(arr):
    h=0
    for i in arr:
        if(i>h):
            h=i
    print("highest element: ",h)        
def low(arr):
    l=0
    for i in arr:
        if(i<l):
            l=i
    print("lowest element: ",l)         

arr=[]
n=int(input("length of array:"))
for j in range(0,n):
    m=int(input())
    arr.append(m)
high(arr) 
low(arr)   
