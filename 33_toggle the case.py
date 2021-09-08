# Write a Programs to toggle the case of characters in String. 
# Uppercasecharacter in string should be converted to lower case and lowercase character toupper case.
n=input("Enter the string: ")
m=""
for i in n:
    if(i.isupper()==True):
        i=i.lower()
        m=m+i
    else:
        i=i.upper()
        m=m+i    

print(m)        