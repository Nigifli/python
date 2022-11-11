number: int = None
 
print("Kérem adjon meg egy számot: ",end="")
number = int(input())

if (number < 0):
    print("A szám negatív.")
elif (number==0):
    print("A szám a 0.")
else:
    print("A szám pozitív.")
