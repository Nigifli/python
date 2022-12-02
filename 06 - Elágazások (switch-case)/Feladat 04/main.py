num1: int=None
num2: int=None
operator: str=None
result: float=None

print("Kérem adjon meg egy számot: ")
num1=int(input())

print("Kérem adjon meg egy másik számot: ")
num2=int(input())

print("Kérem adjon meg egy műveleti jelet: ")
operator=input()

match operator:
    case "+":
        result=num1+num2
    case "-":
        result=num1-num2
    case "*":
        result=num1*num2
    case "/":
        result=num1/num2
    case _:
        print("Nincs ilyen művelet.")

if(result != None):
    print(f"Az eredmény: {result}")