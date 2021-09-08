# Write a program to print the area of two rectangles having sides (4,5) and (5,8) respectively by 
# creating a class named 'Rectangle' with a function named 'Area'which returns the area. 
# Length and breadth are passed as parameters to itsconstructor
def rect(l,b):
    print("area is ",l*b)
l1=int(input("Enter length of 1st rect: "))  
b1=int(input("Enter breadth of 1st rect: "))  
l2=int(input("Enter length of 2nd rect: "))  
b2=int(input("Enter breadth of 2nd rect: "))    
rect(l1,b1)
rect(l2,b2)