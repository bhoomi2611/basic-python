#Rewrite each condition below in valid Java syntax (give a boolean expression):
# x > y > z
x=int(input())
y=int(input())
z=int(input())
if(x>y and y>z):
    print(True)
else:
    print(False)    
# x and y are both less than 0
if(x<0 and y<0):
    print(True)
else:
    print(False)    
# neither x nor y is less than 0
if(x>=0 and y>=0):
    print(True)
else:
    print(False)
# x is equal to y but not equal to z
if(x==y and x!=z):
    print(True)
else:
    print(False)

