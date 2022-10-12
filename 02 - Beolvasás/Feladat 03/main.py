from os import system

name: str=None
height: float=None

print("Kérem adja meg a nevét: ", end="")
name=str(input())

print("Kérem adja meg a magasságát méterben: ", end="")
height=float(input())

system('cls')

print(f"{name} az ön magassága {height}m!")