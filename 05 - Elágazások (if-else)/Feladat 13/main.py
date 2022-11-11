from os import system

number: int = None
 
print("Kérem adjon meg egy számot: ",end="")
number = int(input())

if (number > 0 and number <= 9):
    print("A szám egyjegyű.")
elif(number >= 10 and number <= 99):
    print("A szám kétjegyű.")
elif(number >= 100 and number <= 999):
    print("A szám háromjegyű.")
else:
    print("A szám több, mint háromjegyű.")
