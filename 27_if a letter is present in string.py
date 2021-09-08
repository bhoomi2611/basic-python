#Write a program to check if the letter 'e' is present in the word 'Umbrella'
str1=input("Enter the word: ")
for i in str1:
    if(i=='e' or i=='E'):
        print("yes")
        break
else:
    print("no")        