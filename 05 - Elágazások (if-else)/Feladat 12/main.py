from os import system

number: int = None
 
print("Kérem adjon meg egy számot: ",end="")
number = int(input())

if (number > 10 and number < 20):
    print("A szám 10 és 20 között van.")
elif(number > -20 and number < -10):
    print("A stám -10 és -20 között van.") 
else:
    print("A szám nincs 10 és 20 között, sem -10 és -20 között.")

