from os import system

num1: int=None
num2: int=None

print("Adjon meg egy egész számot: ", end="")
num1 = int(input())

print("Adjon meg egy másik egész számot: ", end="")
num2 = int(input())

if (num1>num2):
    print(f"{num2}, {num1}")

elif (num1 == num2):
    print("A két szám egyenlő.")

else:
    print(f"{num1}, {num2}")