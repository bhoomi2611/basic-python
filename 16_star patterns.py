
# n=int(input())
# m=(2*n)-2
# for i in range(0,n):
#     for j in range(0,m):
#         print(end=" ")
#     m=m-1 
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print(" ") 

# n=int(input())
# k = 2 * n - 2
# for i in range(0, n):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 2
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")

n=int(input())
for i in range(0,n):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(n, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
    
          