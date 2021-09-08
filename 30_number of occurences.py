# Input a string of alphabets. 
# Find out the number of occurrence of all alphabets in that string. 
# Find out the alphabet with maximum occurrence.
n=input("Enter the string")
for i in n:
    count=0
    for k in range(0,len(n)):
        if(i==n[k]):
            count=count+1   
    if(count>0):         
        print(i,"appears in string for",count,"times")    
    n= n.replace(i, '').strip()        