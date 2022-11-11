from os import system

num: int=None

print("Kérem adjon meg egy számot: ", end="")
num=int(input())

if (num%2==0 and num%3==0):
    print("ZIZI")
elif (num%2==0):
    print("BIZ")
elif(num%3==0):
    print("BAZ")
else:
    print("A szám nem osztható sem 3-mal, sem 2-vel.")
