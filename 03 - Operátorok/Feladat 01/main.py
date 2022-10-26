from os import system

firstNumber: int=None
secondNumber: int=None
solution: int=None

print("Kérem adjon meg egy egész számot: ", end="")
firstNumber=int(input())

print("Kérem adjon meg még egy egész számot: ", end="")
secondNumber=int(input())

system('cls')

print(f"A/az {firstNumber} és a/az {secondNumber} összege {firstNumber+secondNumber}.")
