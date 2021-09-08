# Write a Program to print longest word in a sentence.
n=input()
w=n.split()
l=""
for i in w:
    if len(i)>len(l):
        l=i
print(l)        