from os import system

number: int = None
 
print("Kérem adjon meg egy számot: ",end="")
number = int(input())

if (number % 4 == 0 and number % 6 ==0 ):
    print("A szám osztható 4-el és 6-tal is.")
    
else:
    print("A szám nem osztható 4-el és 6-tal is egyszerre.")