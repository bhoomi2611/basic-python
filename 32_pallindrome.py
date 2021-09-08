# Write a Programs to Check whether a string is palindrome or not.
# (A palindromestring is that string which when reversed is same as original string. 
# For example :“aba” is a palindrome whereas “abc” is not.)
n=input("Enter the string: ")
for i in range(0,len(n)):
    if n[i]!=n[len(n)-i-1]:
        print(False)
        break
else:
    print(True)        