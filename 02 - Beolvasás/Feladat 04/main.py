from os import system

name: str=None
pressedButton: str=None

print("Kérem adja meg a nevét: ", end="")
name = str(input())

print("Kérem nyomjon le egy billentyűt: ", end="")
pressedButton=str(input())

system('cls')

print(f"{name} ön a/az {pressedButton} billentyűt nyomta meg!")