from os import system

number: int = None
 
print("Kérem adjon meg egy számot: ",end="")
number = int(input())

if (number % 5 == 0):
    print("A szám osztható 5-tel.")
    
else:
    print("A szám nem osztható 5-tel.")