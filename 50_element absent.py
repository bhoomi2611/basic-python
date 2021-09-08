# Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in the second array
def findMissing(a, b, n, m):
    for i in range(n):
        for j in range(m):
            if (a[i] == b[j]):
                break
 
        if (j == m - 1):
            print(a[i], end = " ")
 
array1=[]
array2=[]
n1=int(input("Enter length of 1st array"))
for i in range(0,n1):
    m=int(input())
    array1.append(m)

n2=int(input("Enter length of 2nd array"))
for i in range(0,n2):
    m=int(input())
    array2.append(m)
findMissing(array1, array2, n1, n2)