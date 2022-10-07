from os import system

name: str=None
pressedButton: str=None

print("Kérem adja meg a nevét: ")
name = str(input())

print("Kérem nyomjon le egy billentyűt: ")
pressedButton=str(input())

system('cls')

print(f"{name} ön a/az {pressedButton} billentyűt nyomta meg!")