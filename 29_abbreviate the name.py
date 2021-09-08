# Write a program that takes your full name as input and displays the abbreviations of the 
# first and middle names except the last name which is displayed as it is. 
# For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.
n=input("Enter your name: ")
l = n.split()
new = "" 
for i in range(len(l)-1):
    s = l[i]
    new += (s[0].upper()+'.')
new += l[-1].title()
print(new)