from os import system

firstNumber: int=None
secondNumber: int=None
thirdNumber: int=None
fourthNumber: int=None

print("Kérem adja meg az első számot: ", end="")
firstNumber=int(input())

print("Kérem adja meg a második számot: ", end="")
secondNumber=int(input())

print("Kérem adja meg a harmadik számot: ", end="")
thirdNumber=int(input())

print("Kérem adja meg a negyedik számot: ", end="")
fourthNumber=int(input())

system('cls')

solution: float=(firstNumber+secondNumber) / (thirdNumber-fourthNumber)
print(f"A hányados {solution}.")

