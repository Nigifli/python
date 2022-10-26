from os import system

firstNumber: float=None
secondNumber: float=None
thirdNumber: int=None

print("Kérem adja meg az első számot: ", end="")
firstNumber=float(input())

print("Kérem adja meg a második számot: ", end="")
secondNumber=float(input())

print("Kérem adja meg a harmadik számot: ", end="")
thirdNumber=int(input())

system('cls')

solution: float=((firstNumber+0.5)*(secondNumber-0.7))%thirdNumber
print(f"A kapott eredmény maradéka {solution}.")