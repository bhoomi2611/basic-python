#Write a java program to get a year as input and identify if it is a leap year.
yr=int(input())
if(yr%4==0):
    if(yr%100==0):
        if(yr%400==0):
            print("leap year")
        else:
            print("not leap year")    
    else:
        print("leap year")
else:
    print("not leap year")                