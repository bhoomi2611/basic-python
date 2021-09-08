# Write a program to print the area and perimeter of a triangle having sides of 3, 4and 5 units by 
# creating a class named 'Triangle' with a function to print the area and perimeter
def Triangle(s1,s2,s3):
    perimeter=s1+s2+s3
    sp=perimeter/2
    area=((sp-s1)*(sp-s2)*(sp-s3)*sp)**0.5
    print("perimeter is ",perimeter)
    print("area is ",area)
s1=int(input("Enter 1st side"))
s2=int(input("Enter 2nd side"))
s3=int(input("Enter 3rd side"))
Triangle(s1,s2,s3)
    