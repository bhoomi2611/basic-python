# Check if two String is an anagram of each other.
# (Ananagram of a string is another string that contains the same characters, 
# only the order of characters can be different. For example, “abcd” and “dabc” are ananagram of each other.
def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("Yes")
    else:
        print("No")        

s1 =input("Enter first string")
s2 =input("Enter second string")
check(s1, s2)