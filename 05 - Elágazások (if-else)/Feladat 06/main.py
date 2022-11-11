from os import system

num1: int=None
num2: int=None
num3: int=None

print("Adjon meg egy egész számot: ", end="")
num1 = int(input())

print("Adjon meg egy másik egész számot: ", end="")
num2 = int(input())

print("Adjon meg egy harmadik egész számot: ", end="")
num3 = int(input())

if (num1>num2>num3):
    print(f"{num3}, {num2}, {num1}.")

elif (num1>num3>num2):
    print(f"{num2}, {num3}, {num1}.")
elif (num2>num1>num3):
    print(f"{num3}, {num1}, {num2}.")
elif (num2>num3>num1):
    print(f"{num1}, {num3}, {num2}.")
elif (num3>num2>num1):
    print(f"{num1}, {num2}, {num3}.")
elif (num3>num1>num2):
    print(f"{num2}, {num1}, {num3}.")
elif (num1 == num2 == num3):
    print("A három szám egyenlő.")

