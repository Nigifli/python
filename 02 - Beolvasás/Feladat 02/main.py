from os import system

name: str=None
birthYear: int=None

print("Kérem adja meg a nevet: ", end="")
name=str(input())

print("Kérem adja meg a szuletesi evet: ", end="")
birthYear=int(input())

system('cls')

print(f"{name} ön {birthYear}-ban született!")