#Suppose GPA is a variable containing the grade point average of a student.
# Suppose the goal of a program is to let a student know if he/she made theDean's list 
# (the GPA must be 3.5 or above). 
# Write an if... else... statement thatprints out the appropriate message 
# (either "Congratulations—you made theDean's List" or "Sorry you didn't make the Dean's List").
gpa=float(input())
if(gpa>3.5):
    print("Congratulations—you made theDean's List")
else:
    print("Sorry you didn't make to the Dean's List")    