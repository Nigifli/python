from os import system

firstNumber: int=None
secondNumber: int=None
thirdNumber: int=None

print("Kérem adja meg az első számot: ", end="")
firstNumber=int(input())

print("Kérem adja meg a második számot: ", end="")
secondNumber=int(input())

print("Kérem adja meg a harmadik számot: ", end="")
thirdNumber=int(input())

system('cls')

solution=(firstNumber-secondNumber)*thirdNumber
print(f"A {firstNumber} és {secondNumber} különbségének a {thirdNumber}-vel való szorzata egyenlő {solution}-el.")