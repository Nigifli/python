import math

width: int=None
height: int=None
choice: str=None
result: float=None

print("Adja meg a téglalap hosszát: ")
height=int(input())

print("Adja meg a téglalap szélességét: ")
width=int(input())

print("Kérem válasszon kiszámolható műveletek közül: \nt - terület\nk - kerület\na - átló")
choice=input()

match choice:
    case "t":
        result= width * height
        print(f"A téglalap területe: {result}.")
    case "k":
        result=2 * (width+height)
        print(f"A téglalap kerülete: {result}.")
    case "a":
        result = math.sqrt(math.pow(width, 2)+ math.pow(height, 2))
        print(f"A téglalap átlója: {result}.")
    case _:
        print("Nincs ilyen kiszámolható művelet.")
