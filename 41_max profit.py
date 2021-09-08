#The cost of a stock on each day is given in an array, 
# find the max profit that youcan make by buying and selling in those days. 
# For example, if the given array is{100, 180, 260, 310, 40, 535, 695}, 
# the maximum profit can earned by buying onday 0, selling on day 3. 
# Again buy on day 4 and sell on day 6. 
# If the given arrayof prices is sorted in decreasing order, then profit cannot be earned at a
def maximumProfit(A):
    m = 0
 
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            m=max(m,A[j]-A[i])
 
    print(m)
array=[]
n=int(input("enter length of array"))
for i in range(0,n):
    m=int(input())
    array.append(m) 
maximumProfit(array)       

