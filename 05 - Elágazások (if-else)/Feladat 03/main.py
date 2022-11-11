number: int = None
 
print("Kérem adjon meg egy számot: ",end="")
number = int(input())

if (number < 40 and number > -30):
    print("A szám -30 és 40 között van.")
    
else:
    print("A szám nincs -30 és 40 között.")

