#Write a program to determine the raise and new salary for an employee 
# by adding if ... else statements to compute the raise. 
# The input to the program includes the current annual salary for the employee 
# and a number indicating the performance rating (1=excellent, 2=good, and 3=poor). 
# An employee with a rating of 1 will receive a 6% raise, 
# an employee with a rating of 2 will receive a 4% raise, and 
# one with a rating of 3 will receive a 1.5% raise.
curr=float(input("enter your current salary: "))
rat=int(input("enter the rating(1,2 or 3): "))
if(rat==1):
    salary=(106*curr)/100
elif(rat==2):
    salary=(104*curr)/100   
elif(rat==3):
    salary=(101.5*curr)/100   
else:
    print("not valid")
print("New salary is",salary)    
