from os import system

name: str=None
height: float=None

print("Kérem adja meg a nevét: ")
name=str(input())

print("Kérem adja meg a magasságát méterben: ")
height=float(input())

system('cls')

print(f"{name} az ön magassága {height}m!")