num1: int = None
num2: int=None
 
print("Kérem adjon meg egy számot: ",end="")
num1 = int(input())

print("Kérem adjon meg még egy számot: ",end="")
num2 = int(input())

if (num1 > num2 ):
    print("Az első szám nagyobb mint a második.")

else:
    print("A második szám nagyobb mint az első.")